from pymongo.mongo_client import MongoClient
import pandas as pd 
import json


url="mongodb+srv://shomiya:gkuL26zP8RhHgptF@cluster0.zpm04s2.mongodb.net/?retryWrites=true&w=majority"  

client = MongoClient(url)

DATABASE_NAME="SENSOR_FAULT"
COLLECTION_NAME="waferfault"

df = pd.read_csv("/Users/shomiyachaturvedi/Desktop/sensor project /notebooks/wafer_23012020_041211.csv")

df.head()

df=df.drop("Unnamed: 0",axis=1)

df.head()

json_record=list(json.loads(df.T.to_json()).values())

type(json_record)

client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)