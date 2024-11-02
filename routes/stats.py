from fastapi import APIRouter, Depends
from nba_api.stats.endpoints import PlayerDashboardByYearOverYear
from sqlalchemy.orm import Session
from sqlalchemy import insert
from ..config.db import get_db
from ..config import models
from nba_api.stats.static import players
from .players import fetch_player_info
from ..utils.utils import truncate

router = APIRouter()

@router.get("/{name}", tags=["stats"])
async def get_yearly_stats(name: str, db: Session=Depends(get_db)):
    player = fetch_player_info(name, db)
    # player not found
    if not player:
        return { "status": False, "message": f"{name} not found"}

    stats_exists = db.query(models.Season).filter(models.Season.player_id==player.player_id).first()
    # player found in db
    if stats_exists:
        player_stats = db.query(models.Season).filter(models.Season.player_id==player.player_id).all()
        return { "stats": player_stats }

    indexes = { "year": 1, "GP": 5, "MIN": 9, "PTS": 29, "REB": 21, "AST": 22, "STL": 24, 
            "BLK": 25, "FGM": 10, "FGA": 11, "FG_PCT": 12, "FG3M": 13, "FG3A": 14, "FG3_PCT": 15,
            "FTM": 16, "FTA": 17, "FT_PCT": 18, "OREB": 19, "DREB": 20, "TOV": 23, "PF": 27 }
    stats = []
    player_stats = PlayerDashboardByYearOverYear(player_id=player.player_id).get_dict()['resultSets'][1]['rowSet']
    for i in range(1,len(player_stats)):
        stat = player_stats[i]
        true_shooting = truncate((stat[indexes["PTS"]] / (2 * (stat[indexes["FGA"]] + (0.44 * stat[indexes["FTA"]]))))*100, 1)
        season_id = str(player.player_id) + stat[indexes["year"]]
        season_exists = db.query(models.Season).filter(models.Season.season_id==season_id).first()
        if season_exists:
            continue
        player_obj = models.Season( 
            season_id=season_id, 
            player_id=player.player_id, 
            year=stat[indexes["year"]],
            GP=stat[indexes["GP"]], 
            MIN=stat[indexes["MIN"]], 
            PTS=stat[indexes["PTS"]],
            REB=stat[indexes["REB"]], 
            AST=stat[indexes["AST"]], 
            STL=stat[indexes["STL"]],
            BLK=stat[indexes["BLK"]], 
            FGM=stat[indexes["FGM"]], 
            FGA=stat[indexes["FGA"]],
            FG_PCT=truncate(stat[indexes["FG_PCT"]]*100, 1), 
            FG3M=stat[indexes["FG3M"]], 
            FG3A=stat[indexes["FG3A"]],
            FG3_PCT=truncate(stat[indexes["FG3_PCT"]]*100, 1), 
            FTM=stat[indexes["FTM"]], 
            FTA=stat[indexes["FTA"]],
            FT_PCT=truncate(stat[indexes["FT_PCT"]]*100, 1), 
            TS_PCT=true_shooting,
            OREB=stat[indexes["OREB"]], 
            DREB=stat[indexes["DREB"]],
            TOV=stat[indexes["TOV"]], 
            PF=stat[indexes["PF"]] 
        )
        stats.append(player_obj)
        db.add(player_obj)
        db.commit()
        
    for stat in stats:
        db.refresh(stat)
    player_stats = db.query(models.Season).filter(models.Season.player_id==player.player_id).all()
    
    return { "stats": player_stats }