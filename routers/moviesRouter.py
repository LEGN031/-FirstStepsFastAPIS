from fastapi import APIRouter, Body, HTTPException,Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import HTMLResponse
from Models.models import Movie, MovieUpdate
from auth.jwtHandler import create_access_token, verify_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter(prefix="/movies", responses={404: {"message": "Not Found"}}, tags=["Movies"])
oauth2 = OAuth2PasswordBearer(tokenUrl="login")


router.title = 'Movies API'
router.version = '2.0.0'

movies = [{
    "idMovie": 1,
    "title":"Avatar",
    "year":"2009",
    "category":"Sci-fi"
},
    {
        "idMovie" : 2,
        "title" : "The Godfather",
        "year" : "1972",
        "category" : "Crime"
    },
    {
        "idMovie": 3, 
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
async def current_movie(token: str = Depends(oauth2)):
    try:
        payload = verify_access_token(token)
        idMovie: int = payload.get("sub")
        if idMovie is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    movie = searchById(idMovie)
    if not movie:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return movie


@router.get('/', status_code=200)
async def catalog():
    return movies

@router.get('/{id}', status_code=200)
async def searchById(id: int):
    for i in movies:
        if i["idMovie"] == id:
            return i
    raise HTTPException(status_code=404, detail='Not Found')


@router.get("/category", status_code=200)
async def searchByCategory(category:str):
    results = [i for i in movies if i["category"].lower() == category.lower()]
    if results:
        return results
    raise HTTPException(status_code=404, detail='Not Found')


@router.post("/movies", status_code=201)
async def createMovie(movie : Movie):
    found = False
    for i in movies:
        if i["idMovie"] == movie.id:
            found = True
    if found:
        raise HTTPException(status_code=400, detail= 'Already exists')
    movies.append(movie.model_dump())
    return movie

@router.put("/movies/{id}", status_code=200)
async def updateMovies(id : int, movie : MovieUpdate, form_data: OAuth2PasswordRequestForm = Depends()):
    movie_db = movies.get(form_data.username)
    if not movie_db:
        raise HTTPException(status_code=404, detail='Not Found')
    found = False
    for i in movies:
        if i["idMovie"] == id:
            i["title"] = movie.title
            i["year"] = movie.year
            i["category"] = movie.category
            found = True
    if not found:
        raise HTTPException(status_code=404, detail='Not Found')
    return movies

@router.delete("/movies/{id}", status_code= 200)
async def deleteMovie(id : int):
    found = False
    for i in movies:
        if i["idMovie"] == id:
            movies.remove(i)
            found = True
    if not found:
        raise HTTPException(status_code=404, detail='Not Found') 
    return movies

