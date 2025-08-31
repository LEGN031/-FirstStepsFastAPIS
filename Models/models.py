from pydantic import BaseModel
from typing import Optional
class Movie(BaseModel):
    idMovie: Optional[int] = None 
    title: str
    year: str
    category: str

class MovieUpdate(BaseModel):
    title: str
    year: str
    category: str

class Client(BaseModel):
    idCLient: Optional[int] = None
    name: str


class Compra(BaseModel):
    id: Optional[int] = None
    idMovie: int
    idClient: int