from soupsieve import match
import get_unplayed
import generate_odds
import collect_fixture
import generate_stats
import test_stats
import os
import json

def get_index(team_name):
    index = 0
    for team in teams:
        if team_name == team["team"]:
            return index
    
        index = index+1
    return -1

def get_stats(team):
    # os.remove("stats")
    file = open("stats","r")
    lines = file.readlines()

    count = 0
    index = 0
    for line in lines:
        # print(line)
        # count+= 1
        # index+= 1
        data = json.loads(line.strip())
        # print(data)
        if team == data["team"]:
            return data
    return None    

def max_key(scores):
    if(scores['home'] >= scores['away'] and scores['home'] >= scores['tie']):
        return "H"
    elif(scores['away'] >= scores['home'] and scores['away'] >= scores['tie']):
        return 'A'
    elif(scores['tie'] >= scores['away'] and scores['tie'] >= scores['home']):
        return 'T'
    else:
        return 'N'
    
def generate_weekly(standings,points,max):
    for current_team in standings:
        for i in range(len(points)-1):
            if(points[i]['team'] == current_team['team']):
                curr_max = max
                total = 0
                wins = 0
                losses = 0
                draws = 0
                for current_points in points[i]['results']:
                    if curr_max <= 0:
                        break
                    if current_points["points"] == -1:
                        total = total
                    if current_points["points"] == 3:
                        total = total + 3
                        wins = wins + 1
                    if current_points["points"] == 1:
                        total = total +1 
                        draws = draws + 1     
                    if current_points["points"] == 0:
                        total
                        losses = losses + 1
                    curr_max = curr_max - 1
            
                current_team["Played"] = current_team["Played"] + max
                current_team["W"] = current_team["W"] + wins
                current_team["D"] = current_team["D"] + draws
                current_team["L"] = current_team["L"] + losses
                points = ((3*wins)+(draws))* current_team["Played"]
                current_team["Pts"] = current_team["Pts"] + points
    
    return standings

def sort_standings(standings):
    size = len(standings)
    for i in range(size-1):
        for j in range(0,size-i-1):
            if standings[j]["Pts"] > standings[j+1]["Pts"]:
                standings[j],standings[j+1] = standings[j+1],standings[j]

   
round_results = {
    "29":[],
    "30":[],
    "31":[],
    "32":[],
    "33":[],
    "34":[],
    "35":[],
    "36":[],
    "37":[],
    "38":[],
}

teams = [
    {"id":"50","team":"Manchester City","results": [], "stats":[]},
    {"id":"40", "team": "Liverpool","results": [], "stats":[]},
    {"id":"49", "team": "Chelsea","results": [], "stats":[]},
    {"id":"48", "team": "West Ham","results": [], "stats":[]},
    {"id":"33", "team": "Manchester United","results": [], "stats":[]},
    {"id":"42", "team": "Arsenal","results": [], "stats":[]},
    {"id":"39", "team": "Wolves","results": [], "stats":[]},
    {"id":"47", "team": "Tottenham","results": [], "stats":[]},
    {"id":"51", "team": "Brighton","results": [], "stats":[]},
    {"id":"41", "team": "Southampton","results": [], "stats":[]},
    {"id":"46", "team": "Leicester","results": [], "stats":[]},
    {"id":"66", "team": "Aston Villa","results": [], "stats":[]},
    {"id":"52", "team": "Crystal Palace","results": [], "stats":[]},
    {"id":"55", "team": "Brentford","results": [], "stats":[]},
    {"id":"63", "team": "Leeds","results": [], "stats":[]},
    {"id":"45", "team": "Everton","results": [], "stats":[]},
    {"id":"34", "team": "Newcastle","results": [], "stats":[]},
    {"id":"71", "team": "Norwich","results": [], "stats":[]},
    {"id":"38", "team": "Watford","results": [], "stats":[]},
    {"id":"44", "team": "Burnley","results": [], "stats":[]},
]


round_points = [
    {"id":"50","team":"Manchester City","results": []},
    {"id":"40", "team": "Liverpool","results": []},
    {"id":"49", "team": "Chelsea","results": []},
    {"id":"48", "team": "West Ham","results": []},
    {"id":"33", "team": "Manchester United","results": []},
    {"id":"42", "team": "Arsenal","results": []},
    {"id":"39", "team": "Wolves","results": []},
    {"id":"47", "team": "Tottenham","results": []},
    {"id":"51", "team": "Brighton","results": []},
    {"id":"41", "team": "Southampton","results": []},
    {"id":"46", "team": "Leicester","results": []},
    {"id":"66", "team": "Aston Villa","results": []},
    {"id":"52", "team": "Crystal Palace","results": []},
    {"id":"55", "team": "Brentford","results": []},
    {"id":"63", "team": "Leeds","results": []},
    {"id":"45", "team": "Everton","results": []},
    {"id":"34", "team": "Newcastle","results": []},
    {"id":"71", "team": "Norwich","results": []},
    {"id":"38", "team": "Watford","results": []},
    {"id":"44", "team": "Burnley","results": []},
]

# for team in teams:
#     matches = get_unplayed.get_remaining_fixtures(team["team"])
#     round = 0
#     round = int(matches["round"])
#     for match in matches['fixtures']:
#         round = round+1
#         team1 = match["home"]
#         team2 = match["away"]
#         collect_fixture.collect_fixure(team1, team2)
#         odds = generate_odds.generate_odds()
#         game = {"round":round ,"teams":{"home":team1, "away":team2}, "odds":odds}
#         team["results"].append(game)



# for round in round_results:
#     for team in teams:
#         for game in team["results"]:
#             if(game['round'] == int(round)):
#                 round_results[round].append(game)


# # print(round_results["30"])

# # Generate Weekly Points for each rounds

# for team in round_points:
#     curr_team = team["team"]
#     for current_round in round_results.keys():
#         for fixture in round_results[current_round]:
#             winner = "Winner"
#             error = "Error"

#             if winner in fixture['odds']:
#                 if(team["id"] == str(fixture['odds']['Winner'])):
#                     result = {"round":current_round, "points":3}
#                     team["results"].append(result)
#                     break
#                 else:
#                     result = {"round":current_round, "points":0}
#                     team["results"].append(result)
#                     break
            
#             if error in fixture['odds']:
#                 result = {"round":current_round, "points":-1}
#                 team["results"].append(result)
#                 break
            
#             max = max_key(fixture['odds'])
#             if curr_team == fixture['teams']['home']:
#                 if max == 'H':
#                     result = {"round":current_round, "points":3}
#                     team["results"].append(result)
#                     break
#                 elif max == 'A':
#                     result = {"round":current_round, "points":0}
#                     team["results"].append(result)
#                     break
#             elif curr_team == fixture['teams']['away']:
#                 if max == 'A':
#                     result = {"round":current_round, "points":3}
#                     team["results"].append(result)
#                     break
#                 elif max == 'H':
#                     result = {"round":current_round, "points":0}
#                     team["results"].append(result)
#                     break
#             else:
#                 result = {"round":current_round, "points":1}
#                 team["results"].append(result)
#                 break 
                
# print(round_points[0]["results"])

# # Generate Weekly Tables

# current_standings = [
#     {"id":"50","team":"Manchester City","Played":28, "W":0, "D":0, "L":0, "Pts":0},
#     {"id":"40", "team": "Liverpool","Played":28, "W":0, "D":0, "L":0, "Pts":0},
#     {"id":"49", "team": "Chelsea","Played":28, "W":0, "D":0, "L":0, "Pts":0},
#     {"id":"48", "team": "West Ham","Played":28, "W":0, "D":0, "L":0, "Pts":0},
#     {"id":"33", "team": "Manchester United","Played":28, "W":0, "D":0, "L":0, "Pts":0},
#     {"id":"42", "team": "Arsenal","Played":28, "W":0, "D":0, "L":0, "Pts":0},
#     {"id":"39", "team": "Wolves","Played":28, "W":0, "D":0, "L":0, "Pts":0},
#     {"id":"47", "team": "Tottenham","Played":28, "W":0, "D":0, "L":0, "Pts":0},
#     {"id":"51", "team": "Brighton","Played":28, "W":0, "D":0, "L":0, "Pts":0},
#     {"id":"41", "team": "Southampton","Played":28, "W":0, "D":0, "L":0, "Pts":0},
#     {"id":"46", "team": "Leicester","Played":28, "W":0, "D":0, "L":0, "Pts":0},
#     {"id":"66", "team": "Aston Villa","Played":28, "W":0, "D":0, "L":0, "Pts":0},
#     {"id":"52", "team": "Crystal Palace","Played":28, "W":0, "D":0, "L":0, "Pts":0},
#     {"id":"55", "team": "Brentford","Played":28, "W":0, "D":0, "L":0, "Pts":0},
#     {"id":"63", "team": "Leeds","Played":28, "W":0, "D":0, "L":0, "Pts":0},
#     {"id":"45", "team": "Everton","Played":28, "W":0, "D":0, "L":0, "Pts":0},
#     {"id":"34", "team": "Newcastle","Played":28, "W":0, "D":0, "L":0, "Pts":0},
#     {"id":"71", "team": "Norwich","Played":28, "W":0, "D":0, "L":0, "Pts":0},
#     {"id":"38", "team": "Watford","Played":28, "W":0, "D":0, "L":0, "Pts":0},
#     {"id":"44", "team": "Burnley","Played":28, "W":0, "D":0, "L":0, "Pts":0},
# ]

# new_standings = generate_weekly(current_standings,round_points,3)
# sort_standings(new_standings)
# for current in new_standings:
#     print(current)

                
    
# for game in teams[0]["results"]:
#     print(game,"\n")
    


# game = teams[1]["results"][0]


val = test_stats.generate_stats(28)

print(type(val))

{"home_stats":get_stats(teams[0]["team"]), "away_stats":get_stats(teams[1]["team"])}


# print("\t\tManchester City\t - \tLiverpool")
# print("Possession:\t", stats1["possession"], "\t\t", stats2["possession"])
# print("Total Shots:\t", stats1["total_shots"], "\t\t", stats2["total_shots"])
# print("Shots on targer:\t", stats1["on_target"], "\t\t", stats2["on_target"])
# print("Red Cards:\t", stats1["red_cards"], "\t\t", stats2["red_cards"])
# print("Yellow Cards\t", stats1["yellow_cards"], "\t\t", stats2["yellow_cards"])
# print("Penalties:\t", stats1["penalties"], "\t\t", stats2["penalties"])
# print("Free Kicks:\t", stats1["freekicks"], "\t\t", stats2["freekicks"])
# print("Total Passes:\t", stats1["total_passes"], "\t\t", stats2["total_passes"])
# print("Complete Passes:\t", stats1["complete_passes"], "\t\t", stats2["complete_passes"])

    
# for team in teams.keys():
#     teams[team] = get_unplayed.get_remaining_fixtures(team)

# for team in teams:
#     print(teams[team])
    