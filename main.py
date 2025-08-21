from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from Models.Movies import Movie, MovieUpdate
from typing import List

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
},
    {
        "id" : 2,
        "title" : "The Godfather",
        "year" : "1972",
        "category" : "Crime"
    },
    {
        "id": 3, 
        "title": "Interstellar", 
        "year": "2014", 
        "category": "Sci-fi"}
]

@app.get("/movies", tags=['Get movies'])
def catalog() -> List[Movie]:
    return movies

@app.get("/movies/{id}", tags=['Get movies by id'])
def searchById(id: int) -> Movie:
    for i in movies:
        if i["id"] == id:
            return i
    return {"Error": "Not Found"}


@app.get("/movies/category/{category}", tags=['Ger movies by category'])
def searchByCategory(category:str):
    results = [i for i in movies if i["category"].lower() == category.lower()]
    if results:
        return results
    return {"Error": "Not Found"} 
#the route should be something like http://localhost:8000/movies/?category=Sci-fi query paramether


@app.post("/movies", tags=['AddMovies'])
def createMovie(movie : Movie) -> Movie:
    movies.append(movie.model_dump())
    return movie

'''
@app.post("/movies", tags=['Add movies'])
def createMovie( title : str = Body(), year : str = Body(), category : str = Body()):
    movies.append({
        'id' :  movies[-1]["id"] +1 ,
        'title' : title,
        'year' : year,
        'category' : category
    })

    return movies
'''    

@app.put("/movies/{id}", tags=['Update Movies'])
def updateMovies(id : int, movie : MovieUpdate):
    for i in movies:
        if i["id"] == id:
            i["title"] = movie.title
            i["year"] = movie.year
            i["category"] = movie.category
    return movies

'''
@app.put("/movies/{id}", tags=["Update Movies"])
def updateMovie(id:int , title : str = Body(), year : str = Body(), category : str = Body()):
    for i in movies:
        if i["id"] == id:
            i["title"] = title
            i["year"] = year
            i["category"] = category
    return movies
'''

@app.delete("/movies/{id}", tags=["Delete movies"])
def deleteMovie(id : int):
    for i in movies:
        if i["id"] == id:
            movies.remove(i)
    
    return movies