# import http.client
# from datetime import datetime
# from dotenv import load_dotenv
# import os
# import json

# load_dotenv()
# date = datetime.today().strftime('%Y-%m-%d')
# today = date.replace("-", "/", 2)

# # apiKey = 

# def apiCall(endpoint):
#     conn = http.client.HTTPSConnection("api.sportradar.us")
#     conn.request("GET", endpoint)
#     res = conn.getresponse()
#     return res.read().decode("utf-8")

# # todaysGames = json.loads(apiCall(f"/nba/trial/v5/en/games/{today}/schedule.json?api_key={os.getenv('SPORT_RADAR_API_KEY')}"))

# todaysBox = {
#     "id": "f017f946-4a1e-4fa2-b538-b864c7a1eeb2",
#     "title": "Game 3",
#     "status": "inprogress",
#     "coverage": "full",
#     "neutral_site": "false",
#     "scheduled": "2019-05-04T02:30:00+00:00",
#     "lead_changes": 11,
#     "times_tied": 3,
#     "clock": "7:59",
#     "quarter": 3,
#     "track_on_court": "true",
#     "reference": "0041800233",
#     "entry_mode": "WEBSOCKET",
#     "sr_id": "sr:match:18086741",
#     "time_zones": {
#         "venue": "US/Pacific",
#         "home": "US/Pacific",
#         "away": "US/Mountain"
#     },
#     "home": {
#         "name": "Trail Blazers",
#         "alias": "POR",
#         "market": "Portland",
#         "id": "583ed056-fb46-11e1-82cb-f4ce4684ea4c",
#         "points": 54,
#         "bonus": "false",
#         "sr_id": "sr:team:3414",
#         "reference": "1610612757",
#         "scoring": [
#             {
#                 "type": "quarter",
#                 "number": 1,
#                 "sequence": 1,
#                 "points": 23
#             },
#             {
#                 "type": "quarter",
#                 "number": 2,
#                 "sequence": 2,
#                 "points": 25
#             },
#             {
#                 "type": "quarter",
#                 "number": 3,
#                 "sequence": 3,
#                 "points": 6
#             }
#         ],
#         "leaders": {
#             "points": [
#                 {
#                     "full_name": "CJ McCollum",
#                     "jersey_number": "3",
#                     "id": "bc70a55a-cee0-478f-9a13-cf51c4a4187c",
#                     "position": "G",
#                     "primary_position": "SG",
#                     "sr_id": "sr:player:607968",
#                     "reference": "203468",
#                     "statistics": {
#                         "minutes": "22:35",
#                         "field_goals_made": 4,
#                         "field_goals_att": 10,
#                         "field_goals_pct": 40.0,
#                         "three_points_made": 2,
#                         "three_points_att": 3,
#                         "three_points_pct": 66.7,
#                         "two_points_made": 2,
#                         "two_points_att": 7,
#                         "two_points_pct": 28.6,
#                         "blocked_att": 0,
#                         "free_throws_made": 1,
#                         "free_throws_att": 2,
#                         "free_throws_pct": 50.0,
#                         "offensive_rebounds": 0,
#                         "defensive_rebounds": 4,
#                         "rebounds": 4,
#                         "assists": 1,
#                         "turnovers": 0,
#                         "steals": 0,
#                         "blocks": 0,
#                         "assists_turnover_ratio": 0,
#                         "personal_fouls": 1,
#                         "tech_fouls": 0,
#                         "flagrant_fouls": 0,
#                         "pls_min": -4,
#                         "points": 11,
#                         "double_double": "false",
#                         "triple_double": "false",
#                         "effective_fg_pct": 50.0,
#                         "efficiency": 9,
#                         "efficiency_game_score": 6.7,
#                         "points_in_paint": 4,
#                         "points_in_paint_att": 6,
#                         "points_in_paint_made": 2,
#                         "points_in_paint_pct": 33.3,
#                         "true_shooting_att": 10.88,
#                         "true_shooting_pct": 50.6,
#                         "fouls_drawn": 1,
#                         "offensive_fouls": 0,
#                         "points_off_turnovers": 0,
#                         "second_chance_pts": 0
#                     }
#                 }
#             ],
#             "rebounds": [
#                 {
#                     "full_name": "Enes Kanter",
#                     "jersey_number": "00",
#                     "id": "5fb038ef-a3bf-4f52-afce-4f5bd074bb88",
#                     "position": "C",
#                     "primary_position": "C",
#                     "sr_id": "sr:player:607708",
#                     "reference": "202683",
#                     "statistics": {
#                         "minutes": "21:36",
#                         "field_goals_made": 3,
#                         "field_goals_att": 6,
#                         "field_goals_pct": 50.0,
#                         "three_points_made": 0,
#                         "three_points_att": 0,
#                         "three_points_pct": 0.0,
#                         "two_points_made": 3,
#                         "two_points_att": 6,
#                         "two_points_pct": 50.0,
#                         "blocked_att": 1,
#                         "free_throws_made": 0,
#                         "free_throws_att": 0,
#                         "free_throws_pct": 0.0,
#                         "offensive_rebounds": 1,
#                         "defensive_rebounds": 4,
#                         "rebounds": 5,
#                         "assists": 0,
#                         "turnovers": 1,
#                         "steals": 2,
#                         "blocks": 1,
#                         "assists_turnover_ratio": 0.0,
#                         "personal_fouls": 0,
#                         "tech_fouls": 0,
#                         "flagrant_fouls": 0,
#                         "pls_min": -5,
#                         "points": 6,
#                         "double_double": "false",
#                         "triple_double": "false",
#                         "effective_fg_pct": 50.0,
#                         "efficiency": 10,
#                         "efficiency_game_score": 6.6,
#                         "points_in_paint": 6,
#                         "points_in_paint_att": 6,
#                         "points_in_paint_made": 3,
#                         "points_in_paint_pct": 50.0,
#                         "true_shooting_att": 6.0,
#                         "true_shooting_pct": 50.0,
#                         "fouls_drawn": 1,
#                         "offensive_fouls": 0,
#                         "points_off_turnovers": 0,
#                         "second_chance_pts": 4
#                     }
#                 }
#             ],
#             "assists": [
#                 {
#                     "full_name": "Damian Lillard",
#                     "jersey_number": "0",
#                     "id": "5382cf43-3a79-4a5a-a7fd-153906fe65dd",
#                     "position": "G",
#                     "primary_position": "PG",
#                     "sr_id": "sr:player:607552",
#                     "reference": "203081",
#                     "statistics": {
#                         "minutes": "22:29",
#                         "field_goals_made": 3,
#                         "field_goals_att": 8,
#                         "field_goals_pct": 37.5,
#                         "three_points_made": 0,
#                         "three_points_att": 3,
#                         "three_points_pct": 0.0,
#                         "two_points_made": 3,
#                         "two_points_att": 5,
#                         "two_points_pct": 60.0,
#                         "blocked_att": 0,
#                         "free_throws_made": 4,
#                         "free_throws_att": 4,
#                         "free_throws_pct": 100.0,
#                         "offensive_rebounds": 1,
#                         "defensive_rebounds": 4,
#                         "rebounds": 5,
#                         "assists": 3,
#                         "turnovers": 1,
#                         "steals": 0,
#                         "blocks": 0,
#                         "assists_turnover_ratio": 3.0,
#                         "personal_fouls": 1,
#                         "tech_fouls": 0,
#                         "flagrant_fouls": 0,
#                         "pls_min": -3,
#                         "points": 10,
#                         "double_double": "false",
#                         "triple_double": "false",
#                         "effective_fg_pct": 37.5,
#                         "efficiency": 14,
#                         "efficiency_game_score": 8.2,
#                         "points_in_paint": 2,
#                         "points_in_paint_att": 1,
#                         "points_in_paint_made": 1,
#                         "points_in_paint_pct": 100.0,
#                         "true_shooting_att": 9.76,
#                         "true_shooting_pct": 51.2,
#                         "fouls_drawn": 3,
#                         "offensive_fouls": 0,
#                         "points_off_turnovers": 2,
#                         "second_chance_pts": 2
#                     }
#                 }
#             ]
#         }
#     },
#     "away": {
#         "name": "Nuggets",
#         "alias": "DEN",
#         "market": "Denver",
#         "id": "583ed102-fb46-11e1-82cb-f4ce4684ea4c",
#         "points": 58,
#         "bonus": "false",
#         "sr_id": "sr:team:3417",
#         "reference": "1610612743",
#         "scoring": [
#             {
#                 "type": "quarter",
#                 "number": 1,
#                 "sequence": 1,
#                 "points": 17
#             },
#             {
#                 "type": "quarter",
#                 "number": 2,
#                 "sequence": 2,
#                 "points": 30
#             },
#             {
#                 "type": "quarter",
#                 "number": 3,
#                 "sequence": 3,
#                 "points": 11
#             }
#         ],
#         "leaders": {
#             "points": [
#                 {
#                     "full_name": "Jamal Murray",
#                     "jersey_number": "27",
#                     "id": "685576ef-ea6c-4ccf-affd-18916baf4e60",
#                     "position": "G",
#                     "primary_position": "PG",
#                     "sr_id": "sr:player:996299",
#                     "reference": "1627750",
#                     "statistics": {
#                         "minutes": "21:38",
#                         "field_goals_made": 9,
#                         "field_goals_att": 15,
#                         "field_goals_pct": 60.0,
#                         "three_points_made": 2,
#                         "three_points_att": 5,
#                         "three_points_pct": 40.0,
#                         "two_points_made": 7,
#                         "two_points_att": 10,
#                         "two_points_pct": 70.0,
#                         "blocked_att": 0,
#                         "free_throws_made": 0,
#                         "free_throws_att": 0,
#                         "free_throws_pct": 0.0,
#                         "offensive_rebounds": 2,
#                         "defensive_rebounds": 1,
#                         "rebounds": 3,
#                         "assists": 1,
#                         "turnovers": 0,
#                         "steals": 0,
#                         "blocks": 0,
#                         "assists_turnover_ratio": 0,
#                         "personal_fouls": 1,
#                         "tech_fouls": 0,
#                         "flagrant_fouls": 0,
#                         "pls_min": 10,
#                         "points": 20,
#                         "double_double": "false",
#                         "triple_double": "false",
#                         "effective_fg_pct": 66.7,
#                         "efficiency": 19,
#                         "efficiency_game_score": 15.1,
#                         "points_in_paint": 12,
#                         "points_in_paint_att": 7,
#                         "points_in_paint_made": 6,
#                         "points_in_paint_pct": 85.7,
#                         "true_shooting_att": 15.0,
#                         "true_shooting_pct": 66.7,
#                         "fouls_drawn": 2,
#                         "offensive_fouls": 0,
#                         "points_off_turnovers": 0,
#                         "second_chance_pts": 5
#                     }
#                 }
#             ],
#             "rebounds": [
#                 {
#                     "full_name": "Paul Millsap",
#                     "jersey_number": "4",
#                     "id": "59f6f688-7000-4cf5-a27f-a1980dd86d93",
#                     "position": "F",
#                     "primary_position": "PF",
#                     "sr_id": "sr:player:607780",
#                     "reference": "200794",
#                     "statistics": {
#                         "minutes": "20:15",
#                         "field_goals_made": 4,
#                         "field_goals_att": 9,
#                         "field_goals_pct": 44.4,
#                         "three_points_made": 1,
#                         "three_points_att": 2,
#                         "three_points_pct": 50.0,
#                         "two_points_made": 3,
#                         "two_points_att": 7,
#                         "two_points_pct": 42.9,
#                         "blocked_att": 2,
#                         "free_throws_made": 0,
#                         "free_throws_att": 2,
#                         "free_throws_pct": 0.0,
#                         "offensive_rebounds": 3,
#                         "defensive_rebounds": 5,
#                         "rebounds": 8,
#                         "assists": 1,
#                         "turnovers": 0,
#                         "steals": 2,
#                         "blocks": 0,
#                         "assists_turnover_ratio": 0,
#                         "personal_fouls": 1,
#                         "tech_fouls": 0,
#                         "flagrant_fouls": 0,
#                         "pls_min": -3,
#                         "points": 9,
#                         "double_double": "false",
#                         "triple_double": "false",
#                         "effective_fg_pct": 50.0,
#                         "efficiency": 12,
#                         "efficiency_game_score": 9.4,
#                         "points_in_paint": 6,
#                         "points_in_paint_att": 6,
#                         "points_in_paint_made": 3,
#                         "points_in_paint_pct": 50.0,
#                         "true_shooting_att": 9.88,
#                         "true_shooting_pct": 45.5,
#                         "fouls_drawn": 2,
#                         "offensive_fouls": 0,
#                         "points_off_turnovers": 3,
#                         "second_chance_pts": 2
#                     }
#                 }
#             ],
#             "assists": [
#                 {
#                     "full_name": "Nikola Jokic",
#                     "jersey_number": "15",
#                     "id": "f2625432-3903-4f90-9b0b-2e4f63856bb0",
#                     "position": "C",
#                     "primary_position": "C",
#                     "sr_id": "sr:player:607468",
#                     "reference": "203999",
#                     "statistics": {
#                         "minutes": "25:00",
#                         "field_goals_made": 5,
#                         "field_goals_att": 8,
#                         "field_goals_pct": 62.5,
#                         "three_points_made": 1,
#                         "three_points_att": 1,
#                         "three_points_pct": 100.0,
#                         "two_points_made": 4,
#                         "two_points_att": 7,
#                         "two_points_pct": 57.1,
#                         "blocked_att": 0,
#                         "free_throws_made": 0,
#                         "free_throws_att": 0,
#                         "free_throws_pct": 0.0,
#                         "offensive_rebounds": 2,
#                         "defensive_rebounds": 6,
#                         "rebounds": 8,
#                         "assists": 6,
#                         "turnovers": 4,
#                         "steals": 0,
#                         "blocks": 1,
#                         "assists_turnover_ratio": 1.5,
#                         "personal_fouls": 1,
#                         "tech_fouls": 0,
#                         "flagrant_fouls": 0,
#                         "pls_min": 10,
#                         "points": 11,
#                         "double_double": "false",
#                         "triple_double": "false",
#                         "effective_fg_pct": 68.8,
#                         "efficiency": 18,
#                         "efficiency_game_score": 11.1,
#                         "points_in_paint": 6,
#                         "points_in_paint_att": 5,
#                         "points_in_paint_made": 3,
#                         "points_in_paint_pct": 60.0,
#                         "true_shooting_att": 8.0,
#                         "true_shooting_pct": 68.8,
#                         "fouls_drawn": 0,
#                         "offensive_fouls": 0,
#                         "points_off_turnovers": 0,
#                         "second_chance_pts": 2
#                     }
#                 }
#             ]
#         }
#     }
# }

# for game in todaysGames['games']:
#     if (game['status'] == 'closed'):
#         # gameBoxScore = json.loads(apiCall(f"/nba/trial/v5/en/games/{game['id']}/boxscore.json?api_key={os.getenv('SPORT_RADAR_API_KEY')}"))
#         gameBoxScore = json.loads(todaysBox)
#         print(gameBoxScore)

# # boxscore = apiCall(f"/nba/trial/v5/en/games/f017f946-4a1e-4fa2-b538-b864c7a1eeb2/boxscore.json?api_key={os.getenv('SPORT_RADAR_API_KEY')}")


# # "/nba/trial/v5/en/games/013dd2a7-fec4-4cc5-b819-f3cf16a1f820/boxscore.xml?api_key={your_api_key}"
# # print(schedule)
# # Test Data for schedule

from bs4 import BeautifulSoup
import requests
# Here, we're just importing both Beautiful Soup and the Requests library
page_link = 'https://www.si.com/nba/scoreboard'
# this is the url that we've already determined is safe and legal to scrape from.
page_response = requests.get(page_link, timeout=5)
# here, we fetch the content from the url, using the requests library
page_content = BeautifulSoup(page_response.content, "html.parser")
#we use the html parser to parse the url content and store it in a variable.

# print(page_content)
scores = page_content.find_all('div', class_='scoreboard-game')
# print(scores)
games = []
for x in scores: 
    teams = x.find_all('div', class_='team')
    for y in teams:
        logos
    # team-logo media-img    
    # team-name-container 
    print(teamNames)
# textContent = []
# for i in range(0, 20):
#     paragraphs = page_content.find_all("p")[i].text
#     textContent.append(paragraphs)
# In my use case, I want to store the speech data I mentioned earlier.  so in this example, I loop through the paragraphs, and push them into an array so that I can manipulate and do fun stuff with the data.