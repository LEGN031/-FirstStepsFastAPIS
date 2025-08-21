from fastapi import APIRouter, Body, HTTPException
from fastapi.responses import HTMLResponse
from Models.Movies import Movie, MovieUpdate

router = APIRouter()

router.title = 'Movies API'
router.version = '2.0.0'

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

'''
@router.put("/movies/{id}", tags=["Update Movies"])
def updateMovie(id:int , title : str = Body(), year : str = Body(), category : str = Body()):
    for i in movies:
        if i["id"] == id:
            i["title"] = title
            i["year"] = year
            i["category"] = category
    return movies
'''

'''
@router.post("/movies", tags=['Add movies'])
def createMovie( title : str = Body(), year : str = Body(), category : str = Body()):
    movies.append({
        'id' :  movies[-1]["id"] +1 ,
        'title' : title,
        'year' : year,
        'category' : category
    })

    return movies
'''    

@router.get("/movies", tags=['Get movies'], response_model=list[Movie])
async def catalog():
    return movies

@router.get("/movies/{id}", tags=['Get movies by id'], status_code=200, response_model=Movie)
async def searchById(id: int):
    for i in movies:
        if i["id"] == id:
            return i
    raise HTTPException(status_code=404, detail='Not Found')


@router.get("/movies/category/{category}", tags=['Ger movies by category'], status_code=200, response_model=Movie)
async def searchByCategory(category:str):
    results = [i for i in movies if i["category"].lower() == category.lower()]
    if results:
        return results
    raise HTTPException(status_code=404, detail='Not Found')


@router.post("/movies", tags=['AddMovies'], status_code=201, response_model=Movie)
async def createMovie(movie : Movie):
    for i in movies:
        if i["id"] == movie.id:
            found = True
    if found:
        raise HTTPException(status_code=400, detail= 'Already exists')
    movies.append(movie.model_dump())
    return movie

@router.put("/movies/{id}", tags=['Update Movies'], status_code=200, response_model= list[Movie])
async def updateMovies(id : int, movie : MovieUpdate):
    found = False
    for i in movies:
        if i["id"] == id:
            i["title"] = movie.title
            i["year"] = movie.year
            i["category"] = movie.category
            found = True
    if not found:
        raise HTTPException(status_code=404, detail='Not Found')
    return movies

@router.delete("/movies/{id}", tags=["Delete movies"], status_code= 200, response_model=list[Movie])
async def deleteMovie(id : int):
    found = False
    for i in movies:
        if i["id"] == id:
            movies.remove(i)
            found = True
    if not found:
        raise HTTPException(status_code=404, detail='Not Found') 
    return movies