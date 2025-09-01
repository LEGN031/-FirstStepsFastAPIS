from fastapi import APIRouter, HTTPException
from Models.models import Client, ClientInDB
from db.clientDB import db_client
from db.schemas import client as schema
from bson.objectid import ObjectId 
import hashlib

router = APIRouter(prefix="/clients", responses={404:{ "message": "Not Found"}}, tags=["Clients"])

db = db_client["sample_mflix"]        
users_collection = db["users"]

@router.get("/")
async def home():
    return {"Message" : "Hello Clients"}

def get_password_hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

@router.post("/", status_code=201)
async def createClient(client : ClientInDB):
    client_db = client.model_dump()
    del client_db['clientID']
    client_db["password"] = get_password_hash(client_db["password"])
    users_collection.insert_one(client_db)
    new_client = db_client.local.users.find_one({"username": client_db["username"]})
    return schema.client_schema(new_client)