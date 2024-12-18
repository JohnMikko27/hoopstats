from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from .config import models as models
from .config.db import engine
from .routes.players import router as players_router
from .routes.stats import router as stats_router

def create_unaccent_extension():
    with engine.connect() as connection:
        connection.execute(text("CREATE EXTENSION IF NOT EXISTS unaccent;"))
        connection.commit()

app = FastAPI()

create_unaccent_extension()
models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost:5173",
    "http://localhost:8080",
    "https://hoop-talk.netlify.app",
    "http://localhost:4173"
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





