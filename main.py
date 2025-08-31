from fastapi import FastAPI, Body, HTTPException
from fastapi.responses import HTMLResponse
from routers import clientsRouter, moviesRouter, compraRouter

app = FastAPI()

app.title = 'My first FastAPI api'
app.version = '2.0.0'

app.include_router(clientsRouter.router)
app.include_router(moviesRouter.router)
app.include_router(compraRouter.router)

@app.get("/", )
async def root():
    return {"message": "Hello World"}


'''@app.post("/buy", status_code=200, tags=["Buy a movie"])
async def buyMovie(idMovie: int, idClient: int):
    movie = await moviesRouter.searchById(idMovie)
    client = await clientsRouter.searchById(idClient)
    nueva_compra = {
        "id": len(compraRouter.compras) + 1,
        "idMovie": idMovie,
        "idClient": idClient
    }
    compraRouter.compras.append(nueva_compra)
    return {"message": f"The client {client['name']} bought the movie {movie['title']}"}

@app.get("/byt")
async def buy():
    clientes = clientsRouter.clients
    movies = moviesRouter.movies
    compras = compraRouter.compras
    for i in range(len(compras)):
        for j in range(len(clientes)):
            if compras[i]["idClient"] == clientes[j]["idClient"]:
                for k in range(len(movies)):
                    if compras[i]["idMovie"] == movies[k]["idMovie"]:
                        return {"message": f"The client {clientes[j]['name']} bought the movie {movies[k]['title']}"}
    return {"message": "No purchases found"}
            '''