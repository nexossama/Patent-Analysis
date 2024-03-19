from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import csv
import time


option=Options()
option.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=option)
driver.get("https://ppubs.uspto.gov/pubwebapp/static/pages/ppubsbasic.html")
driver.maximize_window()

search_term1 = "ai"
search_term2 = "education"

search_box1 = driver.find_element(By.ID, "searchText1")
search_box2 = driver.find_element(By.ID, "searchText2")
# Send the search term to the search box
search_box1.send_keys(search_term1)
search_box2.send_keys(search_term2)

# Locate the button (replace with actual HTML element identifiers)
button = driver.find_element(By.ID, "basicSearchBtn") 

for _ in range(10):
    try:
        # Wait for the tag to appear
        button.click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "even")))  # Replace with actual tag name
        break  # If the tag is found, break the loop
        
    except:
        try:
          buttonOK = driver.find_element(By.CLASS_NAME,"QSIWebResponsiveDialog-Layout1-SI_7WgrKZZwMjtuFh4_button QSIWebResponsiveDialog-Layout1-SI_7WgrKZZwMjtuFh4_button-medium QSIWebResponsiveDialog-Layout1-SI_7WgrKZZwMjtuFh4_button-border-radius-slightly-rounded")
        except:# If the tag is not found, click the button and wait for 30 seconds
           time.sleep(10)

# open a csv file to write the results
with open(f'patents_{search_term1}_{search_term2}.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(["id", "Patent number", "link", "title", "inventor name", "date", "num pages"])
    for i in range(67):
      button = driver.find_element(By.XPATH, "//li[@id='paginationNextItem']/a")
      button.click()
      time.sleep(5)
    for i in range(163-67):
      # Get all the tr elements
      rows = driver.find_elements(By.XPATH, "//tbody/tr")

      # Loop through each tr element
      for row in rows:
        # Get the td elements in the current tr element
        cols = row.find_elements(By.TAG_NAME, "td")

        # Check if cols has at least 7 elements
        if len(cols) >= 7:
            # Extract the data from the td elements
            id = cols[0].text
            PatentNumber = cols[1].text
            Link = cols[2].find_element(By.TAG_NAME, "a").get_attribute("href")
            Title = cols[3].text
            InventorName = cols[4].text
            Date = cols[5].text
            NumPages = cols[6].text

            # Write the data to the CSV file
            writer.writerow([id, PatentNumber, Link, Title, InventorName, Date, NumPages])
        else:
            print("Row does not have the expected number of columns")

          # Write the data to the CSV file
      button = driver.find_element(By.XPATH, "//li[@id='paginationNextItem']/a")
      button.click()
      time.sleep(10)
