class Team():
    def __init__(self, team_id, team_name, team_shortname, team_tla, team_crest, team_found_date, stadium_name, team_website, competitions, coach, squad_data ):
        self.team_id = team_id
        self.team_name = team_name
        self.team_shortname = team_shortname
        self.team_tla = team_tla
        self.team_crest = team_crest
        self.team_found_date = team_found_date
        self.stadium_name = stadium_name
        self.team_website = team_website
        self.competitions = competitions
        self.coach = coach
        self.squad_data = squad_data
        
    def to_dict(self):
        return {
            "team_id": self.team_id,
            "team_name": self.team_name,
            "team_shortname": self.team_shortname,
            "team_tla": self.team_tla,
            "team_crest": self.team_crest,
            "team_found_date": self.team_found_date,
            "stadium_name": self.stadium_name,
            "team_website": self.team_website,
            "competitions": self.competitions,
            "coach": self.coach,
            "squad_data": self.squad_data
        }

class Match():
    def __init__(self, home_team_name, home_team_crest, away_team_name, away_team_crest, matchday, date, status, home_score, away_score):
        self.home_team = {
            "name": home_team_name,
            "crest": home_team_crest
        }
        self.away_team = {
            "name": away_team_name,
            "crest": away_team_crest
        }
        self.matchday = matchday
        self.date = date
        self.status = status
        self.home_score = home_score
        self.away_score = away_score
        
    def to_dict(self):
        return {
            "home_team_name": self.home_team["name"],
            "home_team_crest": self.home_team["crest"],
            "away_team_name": self.away_team["name"],
            "away_team_crest": self.away_team["crest"],
            "matchday_number": self.matchday,
            "date": self.date,
            "status": self.status,
            "home_score": self.home_score,
            "away_score": self.away_score
        }
        
class Standings():
    def __init__(self, season, current_matchday, position, team_name, team_crest, playedGames, won, draw, lost, points, goalsFor, goalsAgainst, goalDifference):
        self.season = season
        self.current_matchday = current_matchday
        self.teamdata = {
            "position": position,
            "team_name": team_name,
            "team_crest": team_crest,
            "playedGames": playedGames,
            "won": won,
            "draw": draw,
            "lost": lost,
            "points": points,
            "goalsFor": goalsFor,
            "goalsAgainst": goalsAgainst,
            "goalDifference": goalDifference
        }
        
    def to_dict(self):
        return {
            "season": self.season,
            "current_matchday": self.current_matchday,
            "position": self.teamdata["position"],
            "team_name": self.teamdata["team_name"],
            "team_crest": self.teamdata["team_crest"],
            "playedGames": self.teamdata["playedGames"],
            "won": self.teamdata["won"],
            "draw": self.teamdata["draw"],
            "lost": self.teamdata["lost"],
            "points": self.teamdata["points"],
            "goalsFor": self.teamdata["goalsFor"],
            "goalsAgainst": self.teamdata["goalsAgainst"],
            "goalDifference": self.teamdata["goalDifference"]
        }
        