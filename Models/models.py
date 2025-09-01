from pydantic import BaseModel
from typing import Optional
class Movie(BaseModel):
    idMovie: Optional[str] = None 
    title: str
    year: str
    category: str

class Client(BaseModel):
    clientID : Optional[str] = None
    username: str
    name: str
    email: str
    disabled: bool = False

class ClientInDB(Client):
    password: str


class Compra(BaseModel):
    id: Optional[int] = None
    idMovie: int
    idClient: int