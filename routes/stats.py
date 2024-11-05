from fastapi import APIRouter, Depends
from nba_api.stats.endpoints import PlayerDashboardByYearOverYear
from sqlalchemy.orm import Session
from sqlalchemy import and_
from ..config.db import get_db
from ..config import models
from nba_api.stats.static import players
from nba_api.stats.endpoints import PlayerCareerStats
from .players import fetch_player_info
from ..utils.utils import truncate


indexes = {
    "player_id": 0,
    "season_id": 1, 
    "league_id": 2, 
    "team_id": 3, 
    "team_abbreviation": 4, 
    "player_age": 5, 
    "GP": 6, 
    "GS": 7, 
    "MIN": 8, 
    "FGM": 9, 
    "FGA": 10, 
    "FG_PCT": 11, 
    "FG3M": 12, 
    "FG3A": 13, 
    "FG3_PCT": 14, 
    "FTM": 15, 
    "FTA": 16, 
    "FT_PCT": 17, 
    "OREB": 18, 
    "DREB": 19, 
    "REB": 20, 
    "AST": 21, 
    "STL": 22, 
    "BLK": 23, 
    "TOV": 24, 
    "PF": 25, 
    "PTS": 26
}
router = APIRouter()

@router.get("/{name}/postseason", tags=["stats"])
async def get_yearly_postseason_stats(name: str, db: Session=Depends(get_db)):
    player = fetch_player_info(name, db)
    player_stats = PlayerCareerStats(player_id=player.player_id).get_dict()["resultSets"][2]["rowSet"]
    # might have to get all the stats and compare to player_stats then i can skip it
    # if not i can add the new stats
    stats_exists = db.query(models.Season).filter(
        and_(
            models.Season.player_id==player.player_id,
            models.Season.post_season==True)
        ).first()
    
    # player found in db
    if stats_exists:
        player_stats = db.query(models.Season).filter(
            and_(
                models.Season.player_id==player.player_id,
                models.Season.post_season==True)
            ).all()
        return { "post_season_stats": player_stats }
    
    stats = []
    for stat in player_stats:
        season_id = str(player.player_id) + stat[indexes["season_id"]] + "post"
        season_exists = db.query(models.Season).filter(
            and_(
                models.Season.season_id==season_id,
                models.Season.post_season==True)
            ).first()
        if season_exists:
            continue
        true_shooting = truncate((stat[indexes["PTS"]] / (2 * (stat[indexes["FGA"]] + (0.44 * stat[indexes["FTA"]]))))*100, 1)
        player_obj = models.Season(
            season_id=season_id,
            player_id=player.player_id,
            year=stat[indexes["season_id"]],
            post_season=True,
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
            TS_PCT=true_shooting,
            FT_PCT=truncate(stat[indexes["FT_PCT"]]*100, 1),
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

    player_stats = db.query(models.Season).filter(
        and_(
            models.Season.player_id==player.player_id,
            models.Season.post_season==True)
        ).all()
    
    return { "post_season_stats": player_stats }

@router.get("/{name}/regseason", tags=["stats"])
async def get_yearly_regseason_stats(name: str, db: Session=Depends(get_db)):
    player = fetch_player_info(name, db)
    player_stats = PlayerCareerStats(player_id=player.player_id).get_dict()["resultSets"][0]["rowSet"]
    # return {"player_stats": player_stats}
    stats_exists = db.query(models.Season).filter(
        and_(
            models.Season.player_id==player.player_id,
            models.Season.post_season==False)
        ).first()
    
    # player found in db
    if stats_exists:
        player_stats = db.query(models.Season).filter(
            and_(
                models.Season.player_id==player.player_id,
                models.Season.post_season==False)
            ).all()
        return { "reg_season_stats": player_stats }
    
    stats = []
    for stat in player_stats:
        season_id = str(player.player_id) + stat[indexes["season_id"]]
        season_exists = db.query(models.Season).filter(
            and_(
                models.Season.season_id==season_id,
                models.Season.post_season==False)
            ).first()
        if season_exists:
            continue
        true_shooting = truncate((stat[indexes["PTS"]] / (2 * (stat[indexes["FGA"]] + (0.44 * stat[indexes["FTA"]]))))*100, 1)
        player_obj = models.Season(
            season_id=season_id,
            player_id=player.player_id,
            year=stat[indexes["season_id"]],
            post_season=False,
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
            TS_PCT=true_shooting,
            FT_PCT=truncate(stat[indexes["FT_PCT"]]*100, 1),
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

    player_stats = db.query(models.Season).filter(
        and_(
            models.Season.player_id==player.player_id,
            models.Season.post_season==False)
        ).all()
    
    return { "reg_season_stats": player_stats }

# add post season yearly stats also, i think i have to use the playercareerstats endpoint
# @router.get("/{name}", tags=["stats"])
# async def get_yearly_stats(name: str, db: Session=Depends(get_db)):
#     player = fetch_player_info(name, db)
#     reg_season_stats = await get_yearly_regseason_stats(player, db)
#     post_season_stats = await get_yearly_postseason_stats(player, db)
#     return { "reg_season_stats": reg_season_stats, "post_season_stats": post_season_stats }