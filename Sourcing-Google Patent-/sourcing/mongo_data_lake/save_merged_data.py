from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import pandas as pd

uri = "mongodb+srv://aymanemaghouti:FwbFRrymX6wjJPxG@patents.js05fnq.mongodb.net/?retryWrites=true&w=majority&appName=Patents"

client = MongoClient(uri, server_api=ServerApi('1'))


db = client['patent_db']
collection = db['raw-data-stage-0']

# List to store DataFrames from each collection

cursor = collection.find({})
df = pd.DataFrame(list(cursor))

# Concatenate DataFrames from all collections into one
merged_df = pd.concat(df, ignore_index=True)

# Save the merged DataFrame to a new CSV file
merged_csv = merged_df.to_csv(index=False)


output_collection = db['raw-data-stage-1']
output_collection.insert_one({'csv_data': merged_csv})

print("Merged CSV file uploaded successfully to MongoDB Atlas.")
