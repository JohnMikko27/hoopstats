from db import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Boolean


class Player(Base):
    __tablename__ = "Player"

    player_id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    birthdate = Column(DateTime, nullable=False)
    player_headshot_url = Column(String)
    height = Column(String, nullable=False)
    weight = Column(Integer, nullable=False)
    years_in_league = Column(Integer, nullable=False)


class Season(Base):
    __tablename__ = "Season"

    season_id = Column(String, primary_key=True, nullable=False)
    player_id = Column(Integer, ForeignKey("Player.player_id"))
    year = Column(String, nullable=False)
    post_season = Column(Boolean, nullable=False)
    
    GP = Column(Integer)
    MIN = Column(Integer)
    PTS = Column(Integer)
    REB = Column(Integer)
    AST = Column(Integer)
    STL = Column(Integer)
    BLK = Column(Integer)
    FGM = Column(Integer)
    FGA = Column(Integer)
    FG_PCT = Column(Float)
    FG3M = Column(Integer)
    FG3A = Column(Integer)
    FG3_PCT = Column(Float)
    FTM = Column(Integer)
    FTA = Column(Integer)
    FT_PCT = Column(Float)
    TS_PCT = Column(Float)
    OREB = Column(Integer)
    DREB = Column(Integer)
    TOV = Column(Integer)
    PF = Column(Integer)
    


    
