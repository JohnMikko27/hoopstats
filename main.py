from fastapi import FastAPI
from datetime import datetime
import config.models as models
from config.db import engine
models.Base.metadata.create_all(bind=engine)

from nba_api.stats.endpoints import PlayerCareerStats
from nba_api.stats.static import players
from nba_api.stats.endpoints import PlayerDashboardByYearOverYear
from nba_api.stats.endpoints import CommonPlayerInfo


app = FastAPI()

player = players.find_players_by_full_name("leBron JaMeS")[0]
player2 = players.find_players_by_full_name("jrue holiday")[0]
player3 = players.find_players_by_full_name("jaylen brown")[0]
print(player)
player_stats = PlayerCareerStats(player_id=player['id']).career_totals_regular_season.get_dict()
# print(player_stats)

# getting year over year stats
season = '2020-21'  # Specify the season
player_dashboard = PlayerDashboardByYearOverYear(player_id=player['id'], season=season)
years_played = len(player_dashboard.get_dict()['resultSets'][1]['rowSet'])
stats_data = player_dashboard.get_dict()#['resultSets'][1]['rowSet'][8-years_played]

# getting common player info
player_info = CommonPlayerInfo(player_id=player3['id']).get_dict()

@app.get("/")
def getIndex():
    return {"hello": "hi"}

@app.get("/player")
def getPlayer():
    return { "hello": player_info}

@app.get("/career")
def getCareer():
    return {"hello": stats_data}


