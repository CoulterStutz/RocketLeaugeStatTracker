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

# Open files in write mode
v1RankFile = open("out/1v1rank.txt", "w")
v1DivisionFile = open("out/1v1division.txt", "w")
v1MMRFile = open("out/1v1mmr.txt", "w")
v1StreakFile = open("out/1v1streak.txt", "w")
v1PlayedFile = open("out/1v1played.txt", "w")

v2RankFile = open("out/2v2rank.txt", "w")
v2DivisionFile = open("out/2v2division.txt", "w")
v2MMRFile = open("out/2v2mmr.txt", "w")
v2StreakFile = open("out/2v2streak.txt", "w")
v2PlayedFile = open("out/2v2played.txt", "w")

v3RankFile = open("out/3v3rank.txt", "w")
v3DivisionFile = open("out/3v3division.txt", "w")
v3MMRFile = open("out/3v3mmr.txt", "w")
v3StreakFile = open("out/3v3streak.txt", "w")
v3PlayedFile = open("out/3v3played.txt", "w")

# Initialize API with extracted data
api = RocketLeague(player_name=TrackingConfig["Self"]["PlayerName"], apiSettings=api, trackingSettings=TrackingConfig)

while True:
    api_output = api.makeRankedAPIRequest()

    # Check if 'ranks' key exists in the API response
    if 'ranks' in api_output:
        # Extract values for 1v1
        Ranked1v1Division = api_output['ranks'][0].get('division', 'N/A')
        Ranked1v1Played = api_output['ranks'][0].get('played', 'N/A')
        Ranked1v1Rank = api_output['ranks'][0].get('rank', 'N/A')
        Ranked1v1Streak = api_output['ranks'][0].get('streak', 'N/A')
        Ranked1v1MMR = api_output['ranks'][0].get('mmr', 'N/A')

        # Write values for 1v1 to separate files
        v1RankFile.write(f"{Ranked1v1Rank}\n")
        v1DivisionFile.write(f"{Ranked1v1Division}\n")
        v1MMRFile.write(f"{Ranked1v1MMR}\n")
        v1StreakFile.write(f"{Ranked1v1Streak}\n")
        v1PlayedFile.write(f"{Ranked1v1Played}\n")

        # Check if there are more than one rank in the API response
        if len(api_output['ranks']) > 1:
            # Extract values for 2v2
            Ranked2v2Division = api_output['ranks'][1].get('division', 'N/A')
            Ranked2v2Played = api_output['ranks'][1].get('played', 'N/A')
            Ranked2v2Rank = api_output['ranks'][1].get('rank', 'N/A')
            Ranked2v2Streak = api_output['ranks'][1].get('streak', 'N/A')
            Ranked2v2MMR = api_output['ranks'][1].get('mmr', 'N/A')

            # Write values for 2v2 to separate files
            v2RankFile.write(f"{Ranked2v2Rank}\n")
            v2DivisionFile.write(f"{Ranked2v2Division}\n")
            v2MMRFile.write(f"{Ranked2v2MMR}\n")
            v2StreakFile.write(f"{Ranked2v2Streak}\n")
            v2PlayedFile.write(f"{Ranked2v2Played}\n")

            # Check if there are more than two ranks in the API response
            if len(api_output['ranks']) > 2:
                # Extract values for 3v3
                Ranked3v3Division = api_output['ranks'][2].get('division', 'N/A')
                Ranked3v3Played = api_output['ranks'][2].get('played', 'N/A')
                Ranked3v3Rank = api_output['ranks'][2].get('rank', 'N/A')
                Ranked3v3Streak = api_output['ranks'][2].get('streak', 'N/A')
                Ranked3v3MMR = api_output['ranks'][2].get('mmr', 'N/A')

                # Write values for 3v3 to separate files
                v3RankFile.write(f"{Ranked3v3Rank}\n")
                v3DivisionFile.write(f"{Ranked3v3Division}\n")
                v3MMRFile.write(f"{Ranked3v3MMR}\n")
                v3StreakFile.write(f"{Ranked3v3Streak}\n")
                v3PlayedFile.write(f"{Ranked3v3Played}\n")

# Close all files at the end of the script
v1RankFile.close()
v1DivisionFile.close()
v1MMRFile.close()
v1StreakFile.close()
v1PlayedFile.close()

v2RankFile.close()
v2DivisionFile.close()
v2MMRFile.close()
v2StreakFile.close()
v2PlayedFile.close()

v3RankFile.close()
v3DivisionFile.close()
v3MMRFile.close()
v3StreakFile.close()
v3PlayedFile.close()
