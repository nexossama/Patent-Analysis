from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import  csv

uri = "mongodb+srv://aymanemaghouti:FwbFRrymX6wjJPxG@patents.js05fnq.mongodb.net/?retryWrites=true&w=majority&appName=Patents"

client = MongoClient(uri, server_api=ServerApi('1'))


db = client['patent_db']
collection = db['raw-data-stage-0']

def save(input_file):
    # Read the CSV file, skip the first line, and insert its contents into the collection
    with open('path_to_your_csv_file.csv', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        next(reader)  # Skip the first line
        for row in reader:
            collection.insert_one(row)

    # Optionally, print a success message
    print("Data inserted successfully.")

csv_files = ['../csv_files/downloaded_file0.csv','../csv_files/downloaded_file1.csv']

for file in csv_files:
    save(file)


