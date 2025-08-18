from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

app.title = 'My first FastAPI api'
app.version = '2.0.0'

@app.get("/", tags=['Home'])
async def root():
    return {"message": "Hello World"}

@app.post("addUser", tags=['Add User Method'])
async def addUser():
    print('User added')
    return True

movies = [{
    "id": 1,
    "title":"Avatar",
    "year":"2009",
    "category":"Sci-fi"
}]

@app.get("/movies", tags=['Get movies'])
def home():
    return movies

@app.get("/movies/{id}", tags=['Get movies by id'])
def home(id: int):
    for i in movies:
        if i["id"] == id:
            return movies
    return {"Error": "Not Found"}
    