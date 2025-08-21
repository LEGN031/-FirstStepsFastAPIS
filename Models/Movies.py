from pydantic import BaseModel
from typing import Optional
class Movie(BaseModel):
    id: Optional[int] = None 
    title: str
    year: str
    category: str

class MovieUpdate(BaseModel):
    title: str
    year: str
    category: str