# Debug.py
# This houses classes and functions that aid the debugging process
# You can enable the use of this script in __main__.py by tweaking the debug value in config.json
import json
import random
import time

from termcolor import colored

with open('config.json', 'r') as file:
    config_data = json.load(file)
debug = config_data['DebugEnabled']
debug_delay = config_data['DebugDelay']

InteractionTypes = ["FileCreation", "FileWriting", "FileClearing", "FileClosing"]
rocket_league_ranks = [
        "Bronze I",
        "Bronze II",
        "Bronze III",
        "Silver I",
        "Silver II",
        "Silver III",
        "Gold I",
        "Gold II",
        "Gold III",
        "Platinum I",
        "Platinum II",
        "Platinum III",
        "Diamond I",
        "Diamond II",
        "Diamond III",
        "Champion I",
        "Champion II",
        "Champion III",
        "Grand Champion I",
        "Grand Champion II",
        "Grand Champion III",
        "Supersonic Legend"
]

def isDebugEnabled():
    return debug

def debugDelay():
    if isDebugEnabled():
        time.sleep(debug_delay)

def get_debug_stats():
    debug_output = {
        'ranks': [
            {'division': random.randint(1, 4), 'played': random.randint(1, 9999), 'rank': random.choice(rocket_league_ranks), 'playlist': 'Duel (Ranked)', 'mmr': random.randint(1, 999),
             'streak': random.randint(1, 10)},
            {'division': random.randint(1, 4), 'played': random.randint(1, 9999), 'rank': random.choice(rocket_league_ranks), 'playlist': 'Doubles (Ranked)', 'mmr': random.randint(1, 999),
             'streak': random.randint(1, 10)},
            {'division': random.randint(1, 4), 'played': random.randint(1, 9999), 'rank': random.choice(rocket_league_ranks), 'playlist': 'Standard (Ranked)', 'mmr': random.randint(1, 999),
             'streak': random.randint(1, 10)},
        ]
    }

    return debug_output

def debug(interaction_type, interaction_name, interaction_value=None):
    if isDebugEnabled():
        if interaction_type not in InteractionTypes:
            raise "DebugError: Interaction Type Provided is not a valid InteractionType"
        else:
            if interaction_type == InteractionTypes[0]:
                print(colored(f"Created/Opened File {interaction_name}!", 'yellow'))
            elif interaction_type == InteractionTypes[1]:
                print(colored(f"Wrote Value {interaction_value} to file {interaction_name}"))
            elif interaction_type == InteractionTypes[2]:
                print(colored(f"Cleared File {interaction_name}!", 'yellow'))
            elif interaction_type == interaction_type[3]:
                print(colored(f"Closed File {interaction_name}!", 'yellow'))