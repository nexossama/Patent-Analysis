from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json


uri = "mongodb+srv://<username>:<password>.js05fnq.mongodb.net/?retryWrites=true&w=majority&appName=Patents"

client = MongoClient(uri, server_api=ServerApi('1'))



db = client['patent_db']
collection = db['patent_records']

with open('../output.json') as f:
    data = json.load(f)

collection.insert_many(data)

print("Data inserted successfully.")
