# Rocket League Stream Labels Program

## Overview
Rocket League Stream Labels Program is a tool designed for use in OBS, XSplit, Streamlabs OBS, and other recording/streaming software that supports displaying text from files. It provides real-time updates of Rocket League ranks and statistics for use in live streams or recordings.

## Installation + Configuration
### A. Downloading Repository + Dependencies
```commandline
git clone https://github.com/coulterminer/RocketLeaugeStatTracker.git
cd RocketLeaugeStatTracker
pip3 install -r requirements.txt
```

### B. Obtaining an API Key
    1. Sign up for a subscription (pick the free one if you choose) at https://rapidapi.com/rocket-league-rocket-league-default/api/rocket-league1
    2. In the code snippets section of GET RANKS, in the options constant find your API KEY
        It will look something like this
        'X-RapidAPI-Key': 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',

### C. Configuration
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

### D. Running The Script

```commandline
python main.py
```

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
     - Use OCR to get a players username at the start of the match
     - After the username is obtained, it will be ran through the API
     - Then outputted to your out folder

Feel free to contribute, suggest features, or report issues. Let's make Rocket League streaming more engaging and dynamic!

# Support The Project
## Donating Crypto to the Project Wallet
If you are feeling generous and want to donate to the project wallet, here are the addresses below. Thank you for your contribution

| Coin | Wallet |
|------|--------|
| BTC | 1LwkVt6WxYBEWcrn6guMhT1MVngKbT4X7o |
| ETH/BSC/POLY/ECT | 0x3EE4F556aefac6d62800A703dFc2724bdbCa9653 |
| BNB | bnb1w3n9k4clrw54mwrw8uc72582v24s5qlepvsk4s |
| XMR | 48jaZeGVHLY3MgeHNC81TYfK7JygSemS9WyomsACfTfSRWUjosSySYcRNFHfhe7x895XKcBLSyFaG8aGfJdScokE4HWSVcQ |
| SOL | Ag991w5yaQk6GMFkzQbkiyJ6kkK4AGLs3fuG3KjcPaME |
| BCH | bitcoincash:qzpkunkzlg5dna3lx3ysl0c8yh9n3lzlruw3vjdtsy |
| LTC | LdMS23M5Sph6dAjBEXaJMUmXqbAf6pwSuy |
| TRX | TQopjgzAkUJ8xXDexSBfbtkzNMwpAj2LMB |
| NANO | nano_3eo4d1y9iuwnasf68nb1ac9tqi7makba8icyyd4tgthfthb3mba56pp5fq6s |
| BAND | band1lu9k5zqcv6gc36xswjpyrrvsflefhwgz2ae4xc |

**EVM tokens are also accepted**

**your help will help development in the project, allowing for OCR Opponent reconization in the future**
