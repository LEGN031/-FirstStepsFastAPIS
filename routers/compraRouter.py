from fastapi import APIRouter, HTTPException
from Models.models import Compra

router = APIRouter(prefix="/compra", responses={404:{ "message": "Not Found"}}, tags=["Compra"])

compras = [{
    "id": 1,
    "idMovie": 1,
    "idClient": 2
}
]

@router.get("/", status_code=200)
async def getCompras():
    return compras


@router.post("/", status_code=201, response_model=Compra)
async def createCompra(compra: Compra):
    compra = compra.model_dump()   
    compras.append(compra)
    return compra
    