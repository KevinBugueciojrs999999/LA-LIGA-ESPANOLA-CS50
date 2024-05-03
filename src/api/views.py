from api.models import Team, Match, Standings
from datetime import datetime
import requests
import json


headers = { 'X-Auth-Token': '7dbb5d0f6065470180284ad22209a067' }

def get_laliga_teams(parametro = None):
    
    if parametro is None or not parametro:

        uri = 'https://api.football-data.org/v4/competitions/PD/teams'

        response = requests.get(uri, headers=headers)
        
    elif parametro is not None:
        uri = f'https://api.football-data.org/v4/teams/{parametro}'
        
        response = requests.get(uri, headers=headers)
        
    else:
        print(f"Error: {response.status_code}")
        
    teams_data = []
        
    if response.status_code == 200:
        call_data = json.loads(response.text)
        for team in call_data["teams"]:
            team_id = team["id"]
            team_name = team["name"]
            team_shortname = team["shortName"]
            team_tla = team["tla"]
            team_crest = team["crest"]
            team_found_date = team["founded"]
            stadium_name = team["venue"]
            team_website = team["website"]
            competitions = team["runningCompetitions"]
            coach = team["coach"]["name"]
            squad_data = team["squad"]
            
            copa_del_rey = False
            copa_del_rey_data = {
            "id":2079,
            "name":"Copa del Rey",
            "code":"CDR",
            "type":"CUP",
            "emblem":"https://www.celh.es/wp-content/uploads/2020/12/copa-del-rey-logo-866D8EA317-seeklogo.com_.png"
            }
            
            for competition in competitions:
                if competition['name'] == "Copa del Rey":
                    copa_del_rey = True
                    
            if not copa_del_rey:
                competitions.append(copa_del_rey_data)
            else:
                for comp in competitions:
                    if comp['name'] == "Copa del Rey":
                        comp['emblem'] = "https://www.celh.es/wp-content/uploads/2020/12/copa-del-rey-logo-866D8EA317-seeklogo.com_.png"
                
            team_tuple  = Team(team_id, team_name, team_shortname, team_tla, team_crest, team_found_date, stadium_name, team_website, competitions, coach, squad_data)
            teams_data.append(team_tuple.to_dict())
            
        # Ordenar la lista alfabéticamente por el nombre del equipo
        teams_data = sorted(teams_data, key=lambda x: x['team_shortname'])
    
    return teams_data

def get_laliga_matches(matchday = None):
    
    uri = 'https://api.football-data.org/v4/competitions/PD/matches'
    
    if not matchday:
        query_params = {
            'season': 2023,
            'matchday': 1,
        }
    else:
        query_params = {
            'season': 2023,
            'matchday': matchday,
        }
    
    response = requests.get(uri, headers=headers, params=query_params)
    
    matches_data = []
    
    week_days = {
    'Monday': 'Lunes',
    'Tuesday': 'Martes',
    'Wednesday': 'Miércoles',
    'Thursday': 'Jueves',
    'Friday': 'Viernes',
    'Saturday': 'Sábado',
    'Sunday': 'Domingo'
    }
    
    if response.status_code == 200:
        call_data = json.loads(response.text)
        for match in call_data["matches"]:
            home_team_name = match["homeTeam"]["name"]
            home_team_crest = match["homeTeam"]["crest"]
            away_team_name = match["awayTeam"]["name"]
            away_team_crest = match["awayTeam"]["crest"]
            matchday_number = match["matchday"]
            match_date = datetime.strptime(match["utcDate"], '%Y-%m-%dT%H:%M:%SZ')
            week_day = match_date.strftime('%A')
            week_day_translated = week_days[week_day]
            date = match_date.strftime(f'{week_day_translated} %d/%m %H:%M')
            status = match["status"]
            if match["score"]["fullTime"]["home"] == None or match["score"]["fullTime"]["away"] == None:
                home_score = "-"
                away_score = "-"
            else:
                home_score = match["score"]["fullTime"]["home"]
                away_score = match["score"]["fullTime"]["away"]
            
    
            match = Match(home_team_name, home_team_crest, away_team_name, away_team_crest, matchday_number, date, status, home_score, away_score)
            matches_data.append(match.to_dict())
    else:
        print(f"Error: {response.status_code}")
        
    return matches_data

def get_laligastandings():
    uri = 'https://api.football-data.org/v4/competitions/PD/standings'

    response = requests.get(uri, headers=headers)
    
    standings_data = []
    
    if response.status_code == 200:
        call_data = json.loads(response.text)
        
        season = call_data["filters"]["season"]
        current_matchday = call_data["season"]["currentMatchday"]            
            
        for standing in call_data["standings"]:
            for team_data in standing["table"]:
                position = team_data["position"] 
                team_name = team_data["team"]["name"]
                team_crest = team_data["team"]["crest"]
                playedGames = team_data["playedGames"]
                won = team_data["won"]
                draw = team_data["draw"]
                lost = team_data["lost"]
                points = team_data["points"]
                goalsFor = team_data["goalsFor"]
                goalsAgainst = team_data["goalsAgainst"]
                goalDifference = team_data["goalDifference"]
            
                standings = Standings(season, current_matchday, position, team_name, team_crest, playedGames, won, draw, lost, points, goalsFor, goalsAgainst, goalDifference)
                standings_data.append(standings.to_dict())
    else:
        print(f"Error: {response.status_code}")
        
    return standings_data