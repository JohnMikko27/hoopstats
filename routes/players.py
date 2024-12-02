from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from nba_api.stats.static import players
from nba_api.stats.endpoints import CommonPlayerInfo
from sqlalchemy import func
from ..config.db import get_db
from ..config import models
from ..utils.utils import remove_accents, get_player_without_accents

router = APIRouter()

def get_player_headshot_url(player_id):
    return f"https://cdn.nba.com/headshots/nba/latest/1040x760/{player_id}.png"

def fetch_player_info(name: str, db: Session):
    indexes = { "PERSON_ID": 0, "FIRST_NAME": 1, "LAST_NAME": 2, "DISPLAY_FIRST_LAST": 3,
            "BIRTHDATE": 7, "HEIGHT": 11, "WEIGHT": 12, "SEASON_EXP": 13}
    # check if player in db
    player_info = db.query(models.Player).filter(func.lower((func.unaccent(models.Player.full_name)))
                                                 ==remove_accents(name.lower())).first()
    if player_info:
        return player_info
    
    # check if player exists in nba_api
    player_exists = get_player_without_accents(name)
    if player_exists:
        player = CommonPlayerInfo(player_id=player_exists['id']).get_dict()["resultSets"]
        rowSet = player[0]['rowSet'][0]
        player_headshot = get_player_headshot_url(rowSet[indexes["PERSON_ID"]])
        player_info = models.Player(
            player_id=rowSet[indexes["PERSON_ID"]], 
            first_name=(rowSet[indexes["FIRST_NAME"]]),
            last_name=(rowSet[indexes["LAST_NAME"]]), 
            full_name=(rowSet[indexes["DISPLAY_FIRST_LAST"]]),
            birthdate=rowSet[indexes["BIRTHDATE"]], 
            height=rowSet[indexes["HEIGHT"]],
            weight=rowSet[indexes["WEIGHT"]], 
            years_in_league=rowSet[indexes["SEASON_EXP"]], 
            player_headshot_url=player_headshot
        )
        db.add(player_info)
        db.commit()
        db.refresh(player_info)

        return player_info

@router.get("/{name}", tags=["players"])
async def get_player(name: str, db: Session=Depends(get_db)):
    player_info = fetch_player_info(name, db)
    if player_info:
        return { "status": True, "player_info": player_info }
    return { "status": False, "message": "Player not found" }
