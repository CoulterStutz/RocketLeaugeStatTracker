# Rocket League Stream Labels Program

## Overview
Rocket League Stream Labels Program is a tool designed for use in OBS, XSplit, Streamlabs OBS, and other recording/streaming software that supports displaying text from files. It provides real-time updates of Rocket League ranks and statistics for use in live streams or recordings.

## Configuration
All configuration is done in "config.json"

```json
{
  "DebugEnabled": false, // To enable Debug Mode
  "DebugDelay": 5, // Specifies how long to wait before firing requests in debug mode
  "APISettings": {
    "APIKey": "", // Put your API Key from https://rapidapi.com/rocket-league-rocket-league-default/api/rocket-league1
    "RefreshRate": 600 // How long you want to wait in-between requests
  },
  "Tracking": {
    "Self": {
      "PlayerName": "USERNAME"
    }
  },
  "DisplaySettings": {
    "DisplayTextWithLabel": true, // Display text with the values in the file
    "Colors": {
      "DisplayTextWithColor": true,
      "Rank": {
        "Bronze": "#ff8b3d",
        "Silver": "#b5b5b5",
        "Gold": "#ffd53d",
        "Platinum": "#616161",  // The rank colors 
        "Diamond": "#0088ff",
        "Champion": "#af5eff",
        "Grand": "#ff665e",
        "SSL": "#121212"
      },
      "Text": {
        "LabelColor": "#ffffff", // The color of the label
        "Labels": {
          "RankLabelText": "Rank:",
          "DivisionLabelText": "Division:", // Text for values enabled with DisplayTextWithLabel
          "MMRLabelText": "MMR:",
          "PlayedLabelText": "Played:",
          "StreakLabelText": "Current Win Streak:"
        }
      }
    }
  }
}
```

## Installation
### A. Downloading Repository + Dependencies

## Running The Script

## Roadmap

1. **Linux Support**
   - Objective: Enable compatibility with Linux operating systems.
   - Steps:
     - Investigate Linux compatibility issues.
     - Implement necessary adjustments for Linux support.
     - Test and verify functionality on Linux platforms.

2. **Opponent Tracking**
   - Objective: Introduce a feature to track and display information about opponents during Rocket League matches.
   - Steps:
     - Explore Rocket League API capabilities for opponent data retrieval.
     - Design and implement an opponent tracking system.
     - Integrate opponent data into the program's output files.
     - Test and refine the opponent tracking feature.



Feel free to contribute, suggest features, or report issues. Let's make Rocket League streaming more engaging and dynamic!