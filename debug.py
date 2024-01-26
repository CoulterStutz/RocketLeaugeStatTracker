# Debug.py
# This houses classes and functions that aid the debugging process
# You can enable the use of this script in __main__.py by tweaking the debug value in config.json
import json
from termcolor import colored

with open('config.json', 'r') as file:
    config_data = json.load(file)
debug = config_data['DebugEnabled']

InteractionTypes = ["FileCreation", "FileWriting", "FileClearing"]

def isDebugEnabled():
    return debug

def debug(interaction_type, interaction_name, interaction_value=None):
    if isDebugEnabled():
        if interaction_type not in InteractionTypes:
            raise "DebugError: Interaction Type Provided is not a valid InteractionType"
        else:
            if interaction_type == InteractionTypes[0]:
                print(colored(f"Created/Opened File {interaction_name}!", 'yellow'))
            elif interaction_type == InteractionTypes[1]:
                print(colored(f"Wrote Value {interaction_value} to file {interaction_name}"))