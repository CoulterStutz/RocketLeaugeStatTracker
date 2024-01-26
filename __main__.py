import json
import time
from funcs import *
from debug import *
from termcolor import colored
from API import RocketLeague  # Assuming RocketLeague is the correct class in API.py
import os

# Read JSON from file
with open('config.json', 'r') as file:
    config_data = json.load(file)

# Extract relevant data from the config
APISettings = config_data['APISettings']
TrackingConfig = config_data['Tracking']
DisplaySettings = config_data['DisplaySettings']

# Create directories if they don't exist
if not os.path.exists("out"):
    os.mkdir("out")

# Open files in write mode
v1RankFile = open("out/1v1rank.txt", "w")
debug(InteractionTypes[0], "1v1rank.txt")
v1DivisionFile = open("out/1v1division.txt", "w")
debug(InteractionTypes[0], "1v1division.txt")
v1MMRFile = open("out/1v1mmr.txt", "w")
debug(InteractionTypes[0], "1v1mmr.txt")
v1StreakFile = open("out/1v1streak.txt", "w")
debug(InteractionTypes[0], "1v1streak.txt")
v1PlayedFile = open("out/1v1played.txt", "w")
debug(InteractionTypes[0], "1v1played.txt")

v2RankFile = open("out/2v2rank.txt", "w")
debug(InteractionTypes[0], "2v2rank.txt")
v2DivisionFile = open("out/2v2division.txt", "w")
debug(InteractionTypes[0], "2v2division.txt")
v2MMRFile = open("out/2v2mmr.txt", "w")
debug(InteractionTypes[0], "2v2mmr.txt")
v2StreakFile = open("out/2v2streak.txt", "w")
debug(InteractionTypes[0], "2v2streak.txt")
v2PlayedFile = open("out/2v2played.txt", "w")
debug(InteractionTypes[0], "2v2played.txt")

v3RankFile = open("out/3v3rank.txt", "w")
debug(InteractionTypes[0], "3v3rank.txt")
v3DivisionFile = open("out/3v3division.txt", "w")
debug(InteractionTypes[0], "3v3division.txt")
v3MMRFile = open("out/3v3mmr.txt", "w")
debug(InteractionTypes[0], "3v3mmr.txt")
v3StreakFile = open("out/3v3streak.txt", "w")
debug(InteractionTypes[0], "3v3streak.txt")
v3PlayedFile = open("out/3v3played.txt", "w")
debug(InteractionTypes[0], "3v3played.txt")

# Initialize API with extracted data
api = RocketLeague(player_name=TrackingConfig["Self"]["PlayerName"], apiSettings=APISettings, trackingSettings=TrackingConfig)

debugDelay()

while True:
    clear_files()
    if isDebugEnabled():
        print(colored("Making Debug API Request", "cyan"))
        api_output = {
            'ranks': [
                {'division': 4, 'played': 257, 'rank': 'Silver II', 'playlist': 'Duel (Ranked)', 'mmr': 386,
                 'streak': 1},
                {'division': 4, 'played': 85, 'rank': 'Silver III', 'playlist': 'Doubles (Ranked)', 'mmr': 468,
                 'streak': 1},
                {'division': 3, 'played': 15, 'rank': 'Bronze II', 'playlist': 'Standard (Ranked)', 'mmr': 202,
                 'streak': -3}
            ]
        }
    else:
        print(colored("Making API Request", "cyan"))
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
        v1RankFile.write(f"[color={get_rank_color(Ranked1v1Rank)}]{Ranked1v1Rank}\n")
        debug(InteractionTypes[1], "1v1rank.txt", Ranked1v1Rank)
        v1DivisionFile.write(f"{Ranked1v1Division}\n")
        debug(InteractionTypes[1], "1v1division.txt", Ranked1v1Division)
        v1MMRFile.write(f"{Ranked1v1MMR}\n")
        debug(InteractionTypes[1], "1v1mmr.txt", Ranked1v1MMR)
        v1StreakFile.write(f"{Ranked1v1Streak}\n")
        debug(InteractionTypes[1], "1v1streak.txt", Ranked1v1Streak)
        v1PlayedFile.write(f"{Ranked1v1Played}\n")
        debug(InteractionTypes[1], "1v1played.txt", Ranked1v1Played)

        # Check if there are more than one rank in the API response
        if len(api_output['ranks']) > 1:
            # Extract values for 2v2
            Ranked2v2Division = api_output['ranks'][1].get('division', 'N/A')
            Ranked2v2Played = api_output['ranks'][1].get('played', 'N/A')
            Ranked2v2Rank = api_output['ranks'][1].get('rank', 'N/A')
            Ranked2v2Streak = api_output['ranks'][1].get('streak', 'N/A')
            Ranked2v2MMR = api_output['ranks'][1].get('mmr', 'N/A')

            # Write values for 2v2 to separate files
            v2RankFile.write(f"[color={get_rank_color(Ranked2v2Rank)}]{Ranked2v2Rank}\n")
            debug(InteractionTypes[1], "2v2rank.txt", Ranked2v2Rank)
            v2DivisionFile.write(f"{Ranked2v2Division}\n")
            debug(InteractionTypes[1], "2v2division.txt", Ranked2v2Division)
            v2MMRFile.write(f"{Ranked2v2MMR}\n")
            debug(InteractionTypes[1], "2v2mmr.txt", Ranked2v2MMR)
            v2StreakFile.write(f"{Ranked2v2Streak}\n")
            debug(InteractionTypes[1], "2v2streak.txt", Ranked2v2Streak)
            v2PlayedFile.write(f"{Ranked2v2Played}\n")
            debug(InteractionTypes[1], "2v2played.txt", Ranked2v2Played)

            # Check if there are more than two ranks in the API response
            if len(api_output['ranks']) > 2:
                # Extract values for 3v3
                Ranked3v3Division = api_output['ranks'][2].get('division', 'N/A')
                Ranked3v3Played = api_output['ranks'][2].get('played', 'N/A')
                Ranked3v3Rank = api_output['ranks'][2].get('rank', 'N/A')
                Ranked3v3Streak = api_output['ranks'][2].get('streak', 'N/A')
                Ranked3v3MMR = api_output['ranks'][2].get('mmr', 'N/A')

                # Write values for 3v3 to separate files
                v3RankFile.write(f"[color={get_rank_color(Ranked3v3Rank)}]{Ranked3v3Rank}\n")
                debug(InteractionTypes[1], "3v3rank.txt", Ranked3v3Rank)
                v3DivisionFile.write(f"{Ranked3v3Division}\n")
                debug(InteractionTypes[1], "3v3division.txt", Ranked3v3Division)
                v3MMRFile.write(f"{Ranked3v3MMR}\n")
                debug(InteractionTypes[1], "3v3mmr.txt", Ranked3v3MMR)
                v3StreakFile.write(f"{Ranked3v3Streak}\n")
                debug(InteractionTypes[1], "3v3streak.txt", Ranked3v3Streak)
                v3PlayedFile.write(f"{Ranked3v3Played}\n")
                debug(InteractionTypes[1], "3v3played.txt", Ranked3v3Played)
                
                print(colored("Fetched Ranks!", "Green"))

                print("\n1v1 Stats:")
                print("Rank:", Ranked1v1Rank, Ranked1v1Division)
                print("MMR:", Ranked1v1MMR)
                print("Played: ", Ranked1v1Played)

                print("\n2v2 Stats:")
                print("Rank:", Ranked2v2Rank, Ranked2v2Division)
                print("MMR:", Ranked2v2MMR)
                print("Played: ", Ranked2v2Played)

                print("\n3v3 Stats:")
                print("Rank:", Ranked3v3Rank, Ranked3v3Division)
                print("MMR:", Ranked3v3MMR)
                print("Played: ", Ranked3v3Played)
    print("\nRetrieved Stats")
    time.sleep(APISettings["RefreshRate"])

    if not isDebugEnabled():
        os.system("cls")

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
