# Debug.py
# This houses classes and functions that aid the debugging process
# You can enable the use of this script in __main__.py by tweaking the debug value in config.json
import json
import time

from termcolor import colored

with open('config.json', 'r') as file:
    config_data = json.load(file)
debug = config_data['DebugEnabled']
debug_delay = config_data['DebugDelay']

InteractionTypes = ["FileCreation", "FileWriting", "FileClearing", "FileClosing"]

def isDebugEnabled():
    return debug

def debugDelay():
    if isDebugEnabled():
        time.sleep(debug_delay)

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