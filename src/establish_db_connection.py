from pymongo import MongoClient

#deployment
import os

USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
DB_URL = os.environ.get("DB_URL")

#FOR MONGO ATLAS
# from decouple import config

# USERNAME = config("USER")
# PASSWORD = config("PASSWORD")
# DB_URL = config("DB_URL")

# client = MongoClient(f"mongodb+srv://{USERNAME}:{PASSWORD}@{DB_URL}/?retryWrites=true&w=majority")

#local connection
client =  MongoClient("mongodb://localhost:27017/")
database = client.RailRakshak
