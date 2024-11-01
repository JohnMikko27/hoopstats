from fastapi import FastAPI, Depends
from .config import models as models
from .config.db import engine
from .routes.players import router as players_router
from .routes.stats import router as stats_router

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

app.include_router(players_router, prefix="/players", tags=["players"])
app.include_router(stats_router, prefix="/stats", tags=["stats"])

@app.get("/")
def getIndex():
    return {"hello": "hi"}





