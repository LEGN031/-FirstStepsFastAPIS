from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv("./config/.env")


DB_PASSWORD = os.getenv("DB_PASSWORD")


#local
#db_client = MongoClient("mongodb://localhost:27017/")

#remote
db_client = MongoClient(f"mongodb+srv://medinae663_db_user1:{DB_PASSWORD}@cluster0.xrevs3n.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

