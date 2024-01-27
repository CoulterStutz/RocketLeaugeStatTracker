from funcs import open_files, close_files, get_rank_color, clear_files
from debug import debug, InteractionTypes, isDebugEnabled, debugDelay, get_debug_stats
from termcolor import colored
from API import RocketLeague  # Assuming RocketLeague is the correct class in API.py
import os
import json
import time

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

# Initialize API with extracted data
api = RocketLeague(player_name=TrackingConfig["Self"]["PlayerName"], apiSettings=APISettings, trackingSettings=TrackingConfig)

debugDelay()

while True:

    v1RankFile, v1DivisionFile, v1MMRFile, v1StreakFile, v1PlayedFile, \
    v2RankFile, v2DivisionFile, v2MMRFile, v2StreakFile, v2PlayedFile, \
    v3RankFile, v3DivisionFile, v3MMRFile, v3StreakFile, v3PlayedFile = open_files()

    if isDebugEnabled():
        print(colored("Making Debug API Request", "cyan"))
        api_output = get_debug_stats()
    else:
        print(colored("Making API Request", "cyan"))
        api_output = api.makeRankedAPIRequest()

    # Check if 'ranks' key exists in the API response
    if 'ranks' in api_output:
        for mode_index, mode_name in enumerate(['1v1', '2v2', '3v3']):
            if mode_index < len(api_output['ranks']):
                # Extract values for the current mode
                current_mode = api_output['ranks'][mode_index]
                RankedDivision = current_mode.get('division', 'N/A')
                RankedPlayed = current_mode.get('played', 'N/A')
                RankedRank = current_mode.get('rank', 'N/A')
                RankedStreak = current_mode.get('streak', 'N/A')
                RankedMMR = current_mode.get('mmr', 'N/A')

                # Write values for the current mode to separate files
                rank_file, division_file, mmr_file, streak_file, played_file = locals()[f'v{mode_name[0]}RankFile'], \
                                                                               locals()[f'v{mode_name[0]}DivisionFile'], \
                                                                               locals()[f'v{mode_name[0]}MMRFile'], \
                                                                               locals()[f'v{mode_name[0]}StreakFile'], \
                                                                               locals()[f'v{mode_name[0]}PlayedFile']

                rank_file.write(f"[color={get_rank_color(RankedRank)}]{RankedRank}\n")
                debug(InteractionTypes[1], f"{mode_name.lower()}rank.txt", RankedRank)
                rank_file.flush()

                division_file.write(f"{RankedDivision}")
                debug(InteractionTypes[1], f"{mode_name.lower()}division.txt", RankedDivision)
                division_file.flush()

                mmr_file.write(f"{RankedMMR}")
                debug(InteractionTypes[1], f"{mode_name.lower()}mmr.txt", RankedMMR)
                mmr_file.flush()

                streak_file.write(f"{RankedStreak}")
                debug(InteractionTypes[1], f"{mode_name.lower()}streak.txt", RankedStreak)
                streak_file.flush()

                played_file.write(f"{RankedPlayed}")
                debug(InteractionTypes[1], f"{mode_name.lower()}played.txt", RankedPlayed)
                played_file.flush()

                # Additional debug information
                if mode_index == 0:
                    print(colored("Fetched Ranks!", "Green"))

                print(f"\n{mode_name} Stats:")
                print("Rank:", RankedRank, RankedDivision)
                print("MMR:", RankedMMR)
                print("Played: ", RankedPlayed)

    print("\nRetrieved Stats")
    time.sleep(APISettings["RefreshRate"])

    if not isDebugEnabled():
        os.system("cls")

# Close all files at the end of the script
close_files()
