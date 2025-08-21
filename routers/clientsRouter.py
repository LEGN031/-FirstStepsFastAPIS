from fastapi import APIRouter, HTTPException
from Models.Clients import Client

router = APIRouter(prefix="/clients", responses={404:{ "message": "Not Found"}}, tags=["Clients"])

clients = [{
}]

@router.get("/")
async def home():
    return {"Message" : "Hello Clients"}

@router.get("/{id}", status_code=200, response_model=Client)
async def searchById(id: int):
    for i in clients:
        if i["id"] == id:
            return i
    raise HTTPException(status_code=404, detail='Not Found')