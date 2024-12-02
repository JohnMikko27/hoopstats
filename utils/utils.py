import math
import unicodedata
from nba_api.stats.static import players

def truncate(number: float, digits: int):
    nbDecimals = len(str(number).split('.')[1]) 
    if nbDecimals <= digits:
        return number
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

def remove_accents(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

def get_player_without_accents(name):
    all_players = players.get_players()
    for player in all_players:
        if remove_accents(player['full_name'].lower()) == remove_accents(name.lower()):
            return player
    return None
