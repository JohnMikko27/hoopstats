from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..config.db import get_db
from ..config import models
from nba_api.stats.endpoints import PlayerCareerStats
from nba_api.stats.static import players
from nba_api.stats.endpoints import PlayerDashboardByYearOverYear
from nba_api.stats.endpoints import CommonPlayerInfo
from sqlalchemy import func


router = APIRouter()

@router.get("/{name}", tags=["players"])
async def get_player(name: str, db: Session=Depends(get_db)):
    indexes = { "PERSON_ID": 0, "FIRST_NAME": 1, "LAST_NAME": 2, "DISPLAY_FIRST_LAST": 3,
            "BIRTHDATE": 7, "HEIGHT": 11, "WEIGHT": 12, "SEASON_EXP": 13}
    
    player_info = db.query(models.Player).filter(func.lower(models.Player.full_name)==name.lower()).first()
    
    if player_info:
        print('hi')
        return { "player_info": player_info}
    player_exists = players.find_players_by_full_name(name)[0] if players.find_players_by_full_name(name) else None
    if player_exists:
        player = CommonPlayerInfo(player_id=player_exists['id']).get_dict()["resultSets"]
        rowSet = player[0]['rowSet']
        player_info = { "player_id": rowSet[0][indexes["PERSON_ID"]], "first_name": rowSet[0][indexes["FIRST_NAME"]],
                        "last_name": rowSet[0][indexes["LAST_NAME"]], "full_name": rowSet[0][indexes["DISPLAY_FIRST_LAST"]],
                        "birthdate": rowSet[0][indexes["BIRTHDATE"]], "height": rowSet[0][indexes["HEIGHT"]],
                        "weight": rowSet[0][indexes["WEIGHT"]], "years_in_league": rowSet[0][indexes["SEASON_EXP"]]}
        player_obj = models.Player(player_id=player_info["player_id"], first_name=player_info["first_name"], last_name=player_info["last_name"],
                                    full_name=player_info["full_name"], birthdate=player_info["birthdate"], height=player_info["height"],
                                    weight=player_info["weight"], years_in_league=player_info["years_in_league"])
        db.add(player_obj)
        db.commit()
        db.refresh(player_obj)
        return { "player_info": player_obj}

    return { "status": False, "message": "Player not found" }
