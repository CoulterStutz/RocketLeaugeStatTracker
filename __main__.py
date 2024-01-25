import config
import termcolor
import API as a
import os

if not os.path.exists("\\out"):
    os.mkdir("out")
    selfLabels = open("/out/selflabels.txt", "w+")
    selfLabels = open("/out/opponentlables.txt", "w+")
else:
    selfLabels = open("/out/selflabels.txt", "a")
    selfLabels = open("/out/opponentlables.txt", "a")

api = a.RocketLeauge(player_name=config.Tracking.self.username)
print(api.makeAPIRequest())