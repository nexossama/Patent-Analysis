import json
import requests
import os
from bs4 import BeautifulSoup
from google_patent_scraper import scraper_class
from extract_urls import return_urls
from extract_title import extract_title
from extract_applicants import extract_applicants
# Initialize scraper class
scraper = scraper_class(return_abstract=True)


def process_url(url):
    resp = requests.get(url)
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')
    return scraper.process_patent_html(soup)

# List of URLs
url_list = return_urls()



# List to store the dictionaries
result_list = []

# Loop through each URL, process it, and store the result
f=open('codes.txt','r')
old_codes = f.readlines()
l=[]
for i in old_codes:
    j = i.strip()
    l.append(j)

codes = []
for url in url_list:
    result_dict = process_url(url)
    code = url.split("/")[-2]

    if code not in l:
        codes.append(code)
        result_dict['code'] = code
        result_dict['title'] = extract_title(code)
        result_dict['link']=url
        result_dict['source']='google patent'
        result_dict['applicants']=extract_applicants(url)
        result_list.append(result_dict)


    print("------ URL:",url,' -------------')


l=[]
with open('codes.txt','r') as f:
    old_list=f.readlines()
    for i in old_list:
        j = i.strip()
        l.append(j)

new_list = l + codes

new_list.sort()

# Write the sorted list to a text file
with open('codes.txt', 'w') as f:
    for code in new_list:
        f.write(code + '\n')


# Check if the file exists
if os.path.exists('output.json') and os.path.getsize('output.json') > 0:
    # Read existing data from the JSON file
    with open('output.json', 'r') as json_file:
        existing_data = json.load(json_file)
else:
    existing_data = []

existing_data += result_list


# Write the updated data back to the JSON file
with open('output.json', 'w') as json_file:
    json.dump(existing_data, json_file, indent=4)

print("Data appended to output.json")



