import json
from debug import *

with open('config.json', 'r') as file:
    config_data = json.load(file)

DS = config_data['DisplaySettings']


def open_files():
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

def close_files():
    # List of file paths
    file_paths = [
        "out/1v1rank.txt", "out/1v1division.txt", "out/1v1mmr.txt", "out/1v1streak.txt", "out/1v1played.txt",
        "out/2v2rank.txt", "out/2v2division.txt", "out/2v2mmr.txt", "out/2v2streak.txt", "out/2v2played.txt",
        "out/3v3rank.txt", "out/3v3division.txt", "out/3v3mmr.txt", "out/3v3streak.txt", "out/3v3played.txt"
    ]

    # Loop through each file and close it
    for file_path in file_paths:
        if isDebugEnabled():
            debug(InteractionTypes[3], file_path)
        file.close()


def clear_files():
    # List of file paths
    file_paths = [
        "out/1v1rank.txt", "out/1v1division.txt", "out/1v1mmr.txt", "out/1v1streak.txt", "out/1v1played.txt",
        "out/2v2rank.txt", "out/2v2division.txt", "out/2v2mmr.txt", "out/2v2streak.txt", "out/2v2played.txt",
        "out/3v3rank.txt", "out/3v3division.txt", "out/3v3mmr.txt", "out/3v3streak.txt", "out/3v3played.txt"
    ]

    # Loop through each file and clear its content
    for file_path in file_paths:
        with open(file_path, 'w') as file:
            if isDebugEnabled():
                debug(InteractionTypes[2], file_path)
            file.write("")

    close_files()


def get_rank_color(rank: str):
    r = rank.split()[0].lower

    if r == "bronze":
        return DS["Colors"]["Rank"]["Bronze"]
    elif r == "silver":
        return DS["Colors"]["Rank"]["Silver"]
    elif r == "gold":
        return DS["Colors"]["Rank"]["Gold"]
    elif r == "platinum":
        return DS["Colors"]["Rank"]["Platinum"]
    elif r == "diamond":
        return DS["Colors"]["Rank"]["Diamond"]
    elif r == "champion":
        return DS["Colors"]["Rank"]["Champion"]
    elif r == "grand":
        return DS["Colors"]["Rank"]["Grand Champion"]
    elif r == "super":
        return DS["Colors"]["Rank"]["SSL"]


if __name__ == "__main__":  # Debug
    print(get_rank_color("Bronze I"))
    print(get_rank_color("Silver II"))
    print(get_rank_color("Gold III"))
    print(get_rank_color("Platinum IV"))
    print(get_rank_color("Diamond I"))
    print(get_rank_color("Champion II"))
    print(get_rank_color("Grand Champion III"))
    print(get_rank_color("Super Sonic Legend IV"))
