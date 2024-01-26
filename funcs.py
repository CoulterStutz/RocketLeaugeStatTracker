import json
import debug

with open('config.json', 'r') as file:
    config_data = json.load(file)

DS = config_data['DisplaySettings']

def get_rank_color(rank:str):
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
            if debug.isDebugEnabled():
                debug.debug(debug.InteractionTypes[2], file_path)
            file.write("")

if __name__ == "__main__": # Debug
    print(get_rank_color("Bronze I"))
    print(get_rank_color("Silver II"))
    print(get_rank_color("Gold III"))
    print(get_rank_color("Platinum IV"))
    print(get_rank_color("Diamond I"))
    print(get_rank_color("Champion II"))
    print(get_rank_color("Grand Champion III"))
    print(get_rank_color("Super Sonic Legend IV"))