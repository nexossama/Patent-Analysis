import requests
from bs4 import BeautifulSoup
from google_patent_scraper import scraper_class

scraper = scraper_class(return_abstract=True)



def extract_applicants(url):
    resp = requests.get(url)
    html = resp.text
    soup = BeautifulSoup(html, 'html.parser')


    application_span = soup.find('dd', itemprop='events').find('span', itemprop='title')

    application_name = application_span.get_text()

    names = application_name.replace('Application filed by', '').split(',')
    names = [name.strip() for name in names]
    return names



