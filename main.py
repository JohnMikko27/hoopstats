from fastapi import FastAPI
from datetime import datetime
from nba_api.stats.endpoints import PlayerCareerStats
from nba_api.stats.static import players
from nba_api.stats.endpoints import PlayerDashboardByYearOverYear
import models
from db import engine
models.Base.metadata.create_all(bind=engine)


app = FastAPI()



@app.get("/")
def getIndex():
    return {"hello": "hi"}

@app.get("/{name}")
def getName(name: str):
    return {"hello": f"hi there {name}"}


