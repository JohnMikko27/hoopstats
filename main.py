from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import models as models
from .config.db import engine
from .routes.players import router as players_router
from .routes.stats import router as stats_router

# might have to change every relative import in the project to absolute import
# or the reason it's not working is 
# because it doesn't know that it should install the necessary dependencies first then run
# try running the fastapi command and the uvicorn command
# with the uvicorn it runs successfully with absolute imports
# while fastapi doesn't, it runs with relative imports

# or i might be using the wrong .env thingy in db.py

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:5173",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(players_router, prefix="/players", tags=["players"])
app.include_router(stats_router, prefix="/stats", tags=["stats"])

@app.get("/")
def getIndex():
    return {"hello": "hi"}





