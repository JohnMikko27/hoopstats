from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import models as models
from config.db import engine
from routes.players import router as players_router
from routes.stats import router as stats_router

# might have to change every relative import in the project to absolute import

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





