from fastapi import FastAPI, Depends
from .config import models as models
from .config.db import engine
from .routes.players import router as players_router


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(players_router, prefix="/players", tags=["players"])

@app.get("/")
def getIndex():
    return {"hello": "hi"}





