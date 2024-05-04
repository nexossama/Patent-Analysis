import json
import random
import sys
import time

import requests

class Patent:
    def __init__(self,title,code,publication_date,application_date,applicants,inventors,abstract) -> None:
        self.title=title
        self.code=code  
        self.publication_date=publication_date
        self.application_date=application_date
        self.url=f"https://worldwide.espacenet.com/patent/search?q=pn%3D{self.code}"
        self.applicants=applicants
        self.inventors=inventors
        self.abstract=abstract
        self.source="docdb"

    def patent_to_dict(self):
        return{"title":self.title,
               "code":self.code,
               "pub_date":f"{self.publication_date[:4]}-{self.publication_date[4:6]}-{self.publication_date[6:]}",
               "application date":f"{self.application_date[:4]}-{self.application_date[4:6]}-{self.application_date[6:]}",
               "link":self.url,
               "applicants":self.applicants,
               "inventor_name":self.inventors,
               "abstract_text":self.abstract,
               "source":"OPS",
               "assignee_name_orig": [],
               "assignee_name_current": [],"priority_date": "2020-06-09",
               "grant_date": "",
               "filing_date": "",
               "forward_cite_no_family": [],
               "forward_cite_yes_family":[],
               "backward_cite_no_family": [],
               "backward_cite_yes_family": []
               } 
class APIData:
    def __init__(self,json=None) -> None:
        self.data=json
        self.patents=[]
        self.patent_codes=[]
        
    def set_data(self,json) -> None:
        self.data=json 
    
    def load_existing_patents(self,filename):
        with open(f"{filename}.json","r")as f:
            patents=json.load(f)
        
        for p in patents:
            self.patent_codes.append(p["code"])
        
    def patent_to_json(self,filename="data"):
        patents_list=[]
        for p in self.patents:
            patents_list.append(p.patent_to_dict())
        with open(f"{filename}.json","w")as f:
            json.dump(patents_list,f,indent=4)
            
    def get_all_patents(self):
        if self.data is None :
            return
        self.patent=[]
        # Extract relevant information from exchange-documents
        exchange_documents = self.data['ops:world-patent-data']['ops:biblio-search']['ops:search-result']['exchange-documents']

        for doc in exchange_documents:
            exchange_doc = doc['exchange-document']
            
            country = exchange_doc['@country']
            code = exchange_doc['@doc-number']
            kind = exchange_doc['@kind']
            
            if f"{country}{code}{kind}" in self.patent_codes:
                continue
            
            publication_date = exchange_doc['bibliographic-data']['publication-reference']['document-id'][0]['date']['$']
            application_date = exchange_doc['bibliographic-data']['application-reference']['document-id'][1]['date']['$']

            if exchange_doc['bibliographic-data'].get('invention-title') is None:
                title=""
            else:  
                titles = exchange_doc['bibliographic-data']['invention-title']
                if isinstance(titles,list):
                    title=None
                    for i in titles :
                        if i["@lang"]=="en":
                            title=i["$"]
                    if title==None:
                        title=titles["$"]
                else:
                    title=titles["$"]
            
            applicants_list = []
            applicants=exchange_doc['bibliographic-data']['parties'].get('applicants')
            if applicants is not None :
                applicant = applicants.get('applicant')
                print(country,code,kind)
                if applicant is not None:
                    if isinstance(applicant,list):
                        applicant_data_format=applicant[0]["@data-format"]
                        for appli in applicant:
                            if appli.get('@data-format') == applicant_data_format:
                                name = appli['applicant-name']['name']['$'].replace("\u2002"," ")
                                applicants_list.append(name)
                            else :
                                break
                    else :
                        applicants_list.append(applicant['applicant-name']['name']['$'])
                    
                
            inventors_list = []
            inventors=exchange_doc['bibliographic-data']['parties'].get('inventors')
            if inventors is not None:
                inventor = inventors.get('inventor')
                if inventor is not None:
                    if isinstance(inventor,list):
                        inventor_data_format=inventor[0]["@data-format"]
                        for invent in inventor:
                            if invent.get('@data-format') == inventor_data_format:
                                name = invent['inventor-name']['name']['$'].replace("\u2002"," ")
                                inventors_list.append(name)
                                print("hi")
                            else :
                                break
        
                    else: 
                        inventors_list.append(inventor['inventor-name']['name']['$'].replace("\u2002"," "))
                        


            abstract = ""
            abstracts = exchange_doc.get('abstract')
            if abstracts is not None :
                if isinstance(abstracts,list):
                    abstract=None
                    for i in abstracts :
                        if i["@lang"]=="en":
                            abstract=i["p"]["$"]
                    if abstract==None:
                        abstract=abstracts["p"]["$"]
                else:
                    abstract=abstracts["p"]["$"]
            
            
            
            print("Title:", title)
            print("Country:", country)
            print("Code:", code)
            print("Kind:", kind)
            print("Publication Date:", publication_date)
            print("Application Date:", application_date)
            print("Applicants:", applicants_list)
            print("Inventors:", inventors_list)
            print("Abstract:",abstract)


            print()
            self.patents.append(Patent(title,f"{country}{code}{kind}",publication_date,application_date,applicants_list,inventors_list,abstract))

    
    
class Oauth :
    def __init__(self) -> None:
         self.token=None
        
    def get_token(self) -> str:
        if self.token==None:
            self.set_new_token()
        return self.token

    def set_new_token(self):

        auth_server_url = "https://ops.epo.org/3.2/auth/accesstoken"
        client_id = 'L4FeE3HAELGAAsT15Sf7gMGSQYX9EZeu'
        client_secret = 'v1nQM9kZJNl8FD3L'

        token_req_payload = {'grant_type': 'client_credentials'}

        token_response = requests.post(auth_server_url,
        data=token_req_payload, verify=False, allow_redirects=False,
        auth=(client_id, client_secret))
                    
        if token_response.status_code !=200:
            print("Failed to obtain token from the OAuth 2.0 server", file=sys.stderr)
            sys.exit(1)

        print("Successfuly obtained a new token")
        tokens = json.loads(token_response.text)
        self.token=tokens['access_token']

def get_response(oauth,url):
    token = oauth.get_token()

    api_call_headers = {'Authorization': 'Bearer ' + token,'Accept': 'application/json'}
    api_call_response = requests.get(url, headers=api_call_headers, verify=False)
    print(api_call_response.status_code)
    response=None
    if	api_call_response.status_code == 401:
        oauth.set_new_token()
        token = oauth.get_token()
        time.sleep(2)
        response=get_response(oauth,url)
        return response
    
    print(api_call_response.text)
    return api_call_response.json()
    
def all_request_responses(oauth,apidata,q,filename="data"):
    try:
        start=1
        end=100
        while True :
            response=get_response(oauth,f"http://ops.epo.org/3.2/rest-services/published-data/search/biblio?Range={start}-{end}&q={q}")
            if start == 1:
                total_responses=int(response['ops:world-patent-data']['ops:biblio-search']["@total-result-count"])
                print(total_responses)
                if total_responses==0:
                    break
            apidata.set_data(response)
            apidata.get_all_patents()
            if end<=total_responses:
                start+=100
                end+=100
            else:
                break
            print(f"====={end-100}=======")
            print("total responses : ",total_responses)

            time.sleep(random.randint(1,10))
        apidata.patent_to_json(filename)
    except Exception as e:
        data.get_all_patents()
        apidata.patent_to_json(filename)

    
oauth=Oauth()
data=APIData()
# q1='((ta="artificial intelligence" or ta="AI") or (ta="machine learning") or (ta="deep learning" or ta="DL") ) and (ta="teaching")'
# all_request_responses(oauth,data,q1,"data1")
data.load_existing_patents("data1")
# print(len(data.patent_codes))
# # time.sleep(5)
# # q2='((ta="artificial intelligence" or ta="AI") or (ta="machine learning") or (ta="deep learning" or ta="DL") ) and (ta="education")'
# # all_request_responses(oauth,data,q2,"data2")
data.load_existing_patents("data2")
# # time.sleep(8)
# q3='((ta="artificial intelligence" or ta="AI") or (ta="machine learning") or (ta="deep learning" or ta="DL") ) and (ta="student")'
# all_request_responses(oauth,data,q3,"data3")
data.load_existing_patents("data3")
# print(len(data.patent_codes))
q4='((ta="artificial intelligence" or ta="AI") or (ta="machine learning") or (ta="deep learning" or ta="DL") ) and (ta="classroom")'
all_request_responses(oauth,data,q4,"data4")



