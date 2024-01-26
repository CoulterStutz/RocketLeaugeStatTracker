import requests


class RocketLeague():
    def __init__(self, player_name, apiSettings, trackingSettings):
        self.url = "https://rocket-league1.p.rapidapi.com/ranks/psych0_naught"
        self.rankedheaders = {
            "User-Agent": "RapidAPI Playground",
            "Accept-Encoding": "identity",
            "X-RapidAPI-Key": apiSettings["APIKey"],
            "X-RapidAPI-Host": "rocket-league1.p.rapidapi.com"
        }

        self.player_name = player_name
        self.api = apiSettings
        self.trackingSettings = trackingSettings

    def makeRankedAPIRequest(self):
        response = requests.get(self.url, headers=self.rankedheaders)
        return response.json()