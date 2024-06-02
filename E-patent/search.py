from pymongo import MongoClient
from fuzzywuzzy import fuzz

uri = "mongodb+srv://aymanemaghouti:FwbFRrymX6wjJPxG@patents.js05fnq.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)

db = client["patent_db"]
collection = db["patents"]


def search_title(keyword, offset, limit):
    if keyword == "":
        return list(collection.find({}).skip(offset).limit(limit))
    query = {"title": {"$regex": keyword, "$options": "i"}}
    result = collection.find(query).skip(offset).limit(limit)

    """
    matching_docs = []
    for doc in result:
        if keyword.lower() in doc["title"].lower():
            matching_docs.append(doc)
        else:
            score = fuzz.token_set_ratio(keyword, doc["title"])
            
            threshold = 30
            if score > threshold:
                matching_docs.append(doc)
    """

    return list(result)




