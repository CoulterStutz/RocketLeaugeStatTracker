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