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
