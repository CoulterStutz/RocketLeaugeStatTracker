# Program Name: Config.py
# Program Purpose: To convert the 'config.json' file to be in a class format
import json

class API:
    def __init__(self):
        self.API = {}
        self.RefreshRate = {}

class Tracking:
    class Self:
        def __init__(self):
            self.TrackSelf = {}
            self.TrackTotalGoals = {}
            self.TrackTotalSaves = {}
            self.TrackTotalWins = {}
            self.TrackCurrentRank = {}
            self.TrackGoalAccuracy = {}

    class Opponent:
        def __init__(self):
            self.TrackOpponents = {}
            self.TrackMultipleOpponents = {}
            self.TrackTotalGoals = {}
            self.TrackTotalSaves = {}
            self.TrackTotalWins = {}
            self.TrackCurrentRank = {}
            self.TrackGoalAccuracy = {}

class DisplaySettings:
    class Colors:
        class Rank:
            def __init__(self):
                self.Bronze = {}
                self.Silver = {}
                self.Gold = {}
                self.Platinum = {}
                self.Diamond = {}
                self.Champion = {}
                self.Grand = {}
                self.SSL = {}

        class TextColors:
            def __init__(self):
                self.LabelColor = {}
                self.ValueColor = {}
                self.Empty = {}

# Read JSON from file
with open('config.json', 'r') as file:
    data = json.load(file)

# Create instances of classes
api = API()
api.__dict__ = data['API']

tracking = Tracking()
tracking.Self.__dict__ = data['Tracking']['Self']
tracking.Opponent.__dict__ = data['Tracking']['Opponent']

displaySettings = DisplaySettings()
displaySettings.Colors.Rank.__dict__ = data['DisplaySettings']['Colors']['Rank']
displaySettings.Colors.TextColors.__dict__ = data['DisplaySettings']['Colors']['TextColors']