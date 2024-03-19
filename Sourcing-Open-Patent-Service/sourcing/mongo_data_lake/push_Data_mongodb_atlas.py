from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json


uri = "mongodb+srv://aymanemaghouti:FwbFRrymX6wjJPxG@patents.js05fnq.mongodb.net/?retryWrites=true&w=majority&appName=Patents"

client = MongoClient(uri, server_api=ServerApi('1'))



db = client['patent_db']
collection = db['ops_records']

with open('data3.json') as f:
    data = json.load(f)


print(data)
collection.insert_many(data)

print("Data inserted successfully.")
