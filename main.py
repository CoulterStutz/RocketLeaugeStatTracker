from funcs import open_files, close_files, get_rank_color, clear_files, close_files
from debug import debug, InteractionTypes, isDebugEnabled, debugDelay, get_debug_stats
from termcolor import colored
from API import RocketLeague
import os
import json
import time

# Read JSON from file
with open('config.json', 'r') as file:
    config_data = json.load(file)

# Extract relevant data from the config
APISettings = config_data['APISettings']
DisplaySettings = config_data['DisplaySettings']

# Create directories if they don't exist
if not os.path.exists("out"):
    os.mkdir("out")

# Initialize API with extracted data
api = RocketLeague(player_name=config_data["Tracking"]["Self"]["PlayerName"], apiSettings=APISettings)

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

                label_color = DisplaySettings['Colors']['Text']['LabelColor']

                # Construct the label and value strings
                label_str = DisplaySettings['Colors']['Text']['Labels'].get(f"{mode_name.capitalize()}LabelText", '')
                rank_label_str = DisplaySettings['Colors']['Text']['Labels'].get("RankLabelText", '')
                division_label_str = DisplaySettings['Colors']['Text']['Labels'].get("DivisionLabelText", '')
                mmr_label_str = DisplaySettings['Colors']['Text']['Labels'].get("MMRLabelText", '')
                streak_label_str = DisplaySettings['Colors']['Text']['Labels'].get("StreakLabelText", '')
                played_label_str = DisplaySettings['Colors']['Text']['Labels'].get("PlayedLabelText", '')

                rank_value_str = f"[color={get_rank_color(RankedRank)}]{rank_label_str} {RankedRank}[/color]" if \
                    DisplaySettings['Colors']['DisplayValueWithColor'] else f"{rank_label_str} {RankedRank}"
                division_value_str = f"{division_label_str} {RankedDivision}"
                mmr_value_str = f"{mmr_label_str} {RankedMMR}"
                streak_value_str = f"{streak_label_str} {RankedStreak}"
                played_value_str = f"{played_label_str} {RankedPlayed}"

                # Write values with or without BB code and labels
                if DisplaySettings['DisplayTextWithLabel']:
                    if DisplaySettings['Colors']['DisplayValueWithColor']:
                        rank_file.write(f"[color={label_color}]{label_str} {rank_value_str}[/color]\n")
                        division_file.write(f"[color={label_color}]{label_str} {division_value_str}[/color]\n")
                        mmr_file.write(f"[color={label_color}]{label_str} {mmr_value_str}[/color]\n")
                        streak_file.write(f"[color={label_color}]{label_str} {streak_value_str}[/color]\n")
                        played_file.write(f"[color={label_color}]{label_str} {played_value_str}[/color]\n")

                    else:
                        rank_file.write(f"{label_str} {rank_value_str}\n")
                        division_file.write(f"{label_str} {division_value_str}\n")
                        mmr_file.write(f"{label_str} {mmr_value_str}\n")
                        streak_file.write(f"{label_str} {streak_value_str}\n")
                        played_file.write(f"{label_str} {played_value_str}\n")

                    debug(InteractionTypes[1], f"{mode_name.lower()}rank.txt",
                          f"[color={label_color}]{label_str} {rank_value_str}[/color]")
                    debug(InteractionTypes[1], f"{mode_name.lower()}division.txt",
                          f"[color={label_color}]{label_str} {division_value_str}[/color]")
                    debug(InteractionTypes[1], f"{mode_name.lower()}mmr.txt",
                          f"[color={label_color}]{label_str} {mmr_value_str}[/color]")
                    debug(InteractionTypes[1], f"{mode_name.lower()}streak.txt",
                          f"[color={label_color}]{label_str} {streak_value_str}[/color]")
                    debug(InteractionTypes[1], f"{mode_name.lower()}played.txt",
                          f"[color={label_color}]{label_str} {played_value_str}[/color]")

                    rank_file.flush()
                    division_file.flush()
                    mmr_file.flush()
                    streak_file.flush()
                    played_file.flush()
                else:
                    rank_file.write(f"{rank_value_str}\n")
                    division_file.write(f"{division_value_str}\n")
                    mmr_file.write(f"{mmr_value_str}\n")
                    streak_file.write(f"{streak_value_str}\n")
                    played_file.write(f"{played_value_str}\n")

                    rank_file.flush()
                    division_file.flush()
                    mmr_file.flush()
                    streak_file.flush()
                    played_file.flush()

                # Additional debug information
                if mode_index == 0:
                    print(colored("Fetched Ranks!", "green"))

                print(f"\n{mode_name} Stats:")
                print(f"{rank_value_str}")
                print(f"{division_value_str}")
                print(f"{mmr_value_str}")
                print(f"{streak_value_str}")
                print(f"{played_value_str}")

        print("\nRetrieved Stats")
    else:
        raise Exception("APIERROR: Invalid API Key or Request Limit Reached! Please Wait Before Trying Again")
    time.sleep(APISettings["RefreshRate"])

    if not isDebugEnabled():
        os.system("cls")

# Close all files at the end of the script
close_files()
