import json
import time

import termcolor
from API import RocketLeague  # Assuming RocketLeague is the correct class in API.py
import os

# Read JSON from file
with open('config.json', 'r') as file:
    config_data = json.load(file)

# Extract relevant data from the config
api = config_data['APISettings']
TrackingConfig = config_data['Tracking']
DisplaySettings = config_data['DisplaySettings']

# Create directories if they don't exist
if not os.path.exists("out"):
    os.mkdir("out")

# Open files in append mode
v1RankedFile = open("out/1v1ranked.txt", "a")
v2RankedFile = open("out/2v2ranked.txt", "a")
v3RankedFile = open("out/3v3ranked.txt", "a")

# Initialize API with extracted data
api = RocketLeague(player_name=TrackingConfig["Self"]["PlayerName"], apiSettings=api, trackingSettings=TrackingConfig)

while True:
    api_output = api.makeAPIRequest()
    time.sleep(600)

    Ranked1v1Division = api_output['ranks'][0]['division']
    Ranked1v1Played = api_output['ranks'][0]['played']
    Ranked1v1Rank = api_output['ranks'][0]['rank']
    Ranked1v1Streak = api_output['ranks'][0]['streak']
    Ranked1v1MMR = api_output['ranks'][0]['mmr']

    # Extract values for 2v2
    Ranked2v2Division = api_output['ranks'][1]['division']
    Ranked2v2Played = api_output['ranks'][1]['played']
    Ranked2v2Rank = api_output['ranks'][1]['rank']
    Ranked2v2Streak = api_output['ranks'][1]['streak']
    Ranked2v2MMR = api_output['ranks'][1]['mmr']

    # Extract values for 3v3
    Ranked3v3Division = api_output['ranks'][2]['division']
    Ranked3v3Played = api_output['ranks'][2]['played']
    Ranked3v3Rank = api_output['ranks'][2]['rank']
    Ranked3v3Streak = api_output['ranks'][2]['streak']
    Ranked3v3MMR = api_output['ranks'][2]['mmr']

    v1RankedFile.write(f"1v1 Ranked\nRank: {Ranked1v1Rank}, Division: {Ranked1v1Division} ({Ranked1v1MMR})\nCurrent Win Streak: {Ranked1v1Streak}\nTotal Matches Played: {Ranked1v1Played}")
    v2RankedFile.write(f"2v2 Ranked\nRank: {Ranked2v2Rank}, Division: {Ranked2v2Division} ({Ranked2v2MMR})\nCurrent Win Streak: {Ranked2v2Streak}\nTotal Matches Played: {Ranked2v2Played}\n\n")
    v3RankedFile.write(f"3v3 Ranked\nRank: {Ranked3v3Rank}, Division: {Ranked3v3Division} ({Ranked3v3MMR})\nCurrent Win Streak: {Ranked3v3Streak}\nTotal Matches Played: {Ranked3v3Played}\n\n")

    time.sleep(600)