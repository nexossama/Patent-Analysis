from bson import ObjectId
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://aymanemaghouti:FwbFRrymX6wjJPxG@patents.js05fnq.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("patent_db")

# Access the google_patents collection
patents_collection = db.google_patents

# Assuming 'id' is the ObjectID of the document you want to retrieve
id = '65f93f43618cd872b5ef50d0'

# Query the collection for the document with the given ID
# patent = patents_collection.find_one({'_id': ObjectId(id)})
patent = patents_collection.find()[0]

# Print the retrieved document
print(patent)
