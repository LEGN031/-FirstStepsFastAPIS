from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import hashlib
from auth.jwtHandler import create_access_token, verify_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from datetime import timedelta

router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class Client(BaseModel):
    username: str
    name: str
    email: str
    disabled: bool

class ClientInDB(Client):
    password: str

def get_password_hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return get_password_hash(plain_password) == hashed_password

users_db = {
    "johndoe": {
        "username": "johndoe",
        "name": "John Doe",
        "email": "JohnDoe@gmail.com",
        "disabled": False,
        "password": get_password_hash("123456")
    },
    "janedoe": {
        "username": "janedoe",
        "name": "Jane Doe",
        "email": "JaneDoe@gmail.com",
        "disabled": True,
        "password": get_password_hash("abcdef")
    }
}

def get_user(username: str):
    if username in users_db:
        user_dict = users_db[username]
        return ClientInDB(**user_dict)
    
'''
def verify_user(user: ClientInDB, form_data: OAuth2PasswordRequestForm):
    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail='Incorrect Password')
    return {"access_token": user.username, "token_type": "bearer"}
'''
async def current_user(token: str = Depends(oauth2)):
    try:
        payload = verify_access_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    user = get_user(username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form_data.username)
    if not user_db:
        raise HTTPException(status_code=404, detail='Not Found')
    user = get_user(form_data.username)

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},  # "sub" = subject
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get('/users/me')
async def me(user: Client = Depends(current_user)):
    return Client(**user.model_dump())