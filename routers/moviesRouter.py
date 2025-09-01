from fastapi import APIRouter, Body, HTTPException
from Models.models import Movie
from fastapi.middleware.cors import CORSMiddleware
from db.clientDB import db_client
from db.schemas import movie as schema
from bson.objectid import ObjectId 

router = APIRouter(prefix="/movies", responses={404: {"message": "Not Found"}}, tags=["Movies"])

router.title = 'Movies API'
router.version = '2.0.0'

db = db_client["sample_mflix"]        
movies_collection = db["movies"] 


@router.get('/', status_code=200)
async def catalog():
    movies = movies_collection.find()
    movies = list(map(schema.movie_schema, movies))
    if len(movies) == 0:
        raise HTTPException(status_code=404, detail='Empty List')
    return movies

@router.get("/category", status_code=200)
async def searchByCategory(category:str):
    movies = movies_collection.find({"category": category})
    if movies:
        return list(map(schema.movie_schema, movies))
    raise HTTPException(status_code=404, detail='Not Found')

@router.get('/{id}', status_code=200)
async def searchById(id: str):
    try: 
        oId = ObjectId(id)
    except:
        raise HTTPException(status_code=404, detail='Invalid ID format')
    movie = movies_collection.find_one({"_id": oId})
    if movie:
        return schema.movie_schema(movie)
    raise HTTPException(status_code=404, detail='Not Found')



@router.post("/", status_code=201)
async def createMovie(movie : Movie):
    movie_db = movie.model_dump()
    del movie_db['idMovie']
    movies_collection.insert_one(movie_db)
    new_movie = movies_collection.find_one(movie_db)
    return schema.movie_schema(new_movie)

@router.put("/{id}", status_code=200)
async def updateMovies(id : str, movie : Movie):
    movieUpdate = movies_collection.find_one({"_id": ObjectId(id)})
    if not movieUpdate:
        raise HTTPException(status_code=404, detail='Not Found')
    movies_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": movie.model_dump()})
    movies = movies_collection.find()
    return list(map(schema.movie_schema, movies))

@router.delete("/{id}", status_code= 200)
async def deleteMovie(id : str):
    movie = movies_collection.find_one_and_delete({"_id":ObjectId(id)})
    if not movie:
        raise HTTPException(status_code=404, detail='Not Found')
    movies = movies_collection.find()
    return list(map(schema.movie_schema, movies))

