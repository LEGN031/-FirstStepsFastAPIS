from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import hashlib
from auth.jwtHandler import create_access_token, verify_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta

app = FastAPI()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class Movie(BaseModel):
    idMovie: Optional[int] = None 
    title: str
    year: str
    category: str

movies_db = {
    1: {"idMovie": 1, "title": "Inception", "year": "2010", "category": "Sci-Fi"},
    2: {"idMovie": 2, "title": "The Dark Knight", "year": "2008", "category": "Action"},
    3: {"idMovie": 3, "title": "Interstellar", "year": "2014", "category": "Sci-Fi"}
}

def get_movie(username: str):
    if username in movies_db:
        user_dict = movies_db[username]
        return ClientInDB(**user_dict)