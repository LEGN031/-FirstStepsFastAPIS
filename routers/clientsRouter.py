from fastapi import APIRouter, HTTPException
from Models.models import Client

router = APIRouter(prefix="/clients", responses={404:{ "message": "Not Found"}}, tags=["Clients"])

clients = [{ "idClient": 1, "name": "John Doe" },
           { "idClient": 2, "name": "Jane Doe"
}]

@router.get("/")
async def home():
    return {"Message" : "Hello Clients"}

@router.get("/{id}", status_code=200, response_model=Client)
async def searchById(id: int):
    for i in clients:
        if i["idClient"] == id:
            return i
    raise HTTPException(status_code=404, detail='Not Found')