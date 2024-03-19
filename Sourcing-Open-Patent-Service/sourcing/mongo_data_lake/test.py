from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import  csv



def save(input_file):
    # Read the CSV file and insert its contents into the collection
    # Read the CSV file, skip the first line, and insert its contents into the collection
    with open(input_file, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        next(reader)  # Skip the first line
        for row in reader:
            # Insert each row directly into the collection
            print(row)
    # Optionally, print a success message
    print("Data inserted successfully.")

csv_files = ['../csv_files/downloaded_file0.csv','../csv_files/downloaded_file1.csv']

for file in csv_files:
    save(file)


