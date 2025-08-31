from fastapi import FastAPI, Body, HTTPException
from fastapi.responses import HTMLResponse
from routers import clientsRouter, moviesRouter, compraRouter, basicAuthClients, basicAuthMovies

app = FastAPI()

app.title = 'My first FastAPI api'
app.version = '2.0.0'

app.include_router(clientsRouter.router)
app.include_router(moviesRouter.router)
app.include_router(compraRouter.router)
app.include_router(basicAuthClients.router)

@app.get("/", )
async def root():
    return {"message": "Hello World"}
