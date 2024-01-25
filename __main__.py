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