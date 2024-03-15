# ~ Import packages ~ #
from google_patent_scraper import scraper_class
import json
import requests
from bs4 import BeautifulSoup

# ~ Initialize scraper class ~ #
scraper=scraper_class(return_abstract=True)


url='https://patents.google.com/patent/US11775850B2/en'

resp = requests.get(url)
html = resp.text
soup = BeautifulSoup(html, 'html.parser')


l = scraper.process_patent_html(soup)

print(l)



















# # ~ Get results of scrape ~ #
# patent_1_parsed = scraper.parsed_patents['US11847554B2']
# patent_2_parsed = scraper.parsed_patents['US266827A']







# print(patent_1_parsed)
#
# # ~ Print inventors of patent US2668287A ~ #
# for inventor in json.loads(patent_1_parsed['inventor_name']):
#   print('Patent inventor : {0}'.format(inventor['inventor_name']))