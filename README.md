# MarketWatch-Game-API
Simple API to get statistics from a PUBLIC MarketWatch game and create: Spreadsheets, Weekly/ Daily log files and Graphs

## Installation
The following dependencies must be installed (python 3.8.6):
  - bs4
  - requests
  - openpyxl
  - matplotlib

After, simply clone the repository onto your computer. 


## How to use/ What does it do?
### MWSetup.py
1. Run MWSetup.py (Must be done before anything else) 
2. Edit MWSetup.py to contain the URL of your game
```py
# EDIT BELOW
URL1 = "<GAME URL>"
# EDIT ABOVE
```
Your game URL should look something like this:
> https://www.marketwatch.com/game/padzikintrocohortb/rankings


### MW Weekly.py
1. Enter the week (You shouldn't skip a week; you should start from week 1 and work up)
2. A .txt file will be created in Weekly//LOG that contains the LOG of the week
3. The .xlsx file will be updated to have data about that week

### MW Daily.py
1. Enter the day (You can skip days; but I recommend that you don't)
2. A .txt file will be updated in Daily that contains a dictionary of all players

Note: If a player is removed from the game all previous data in their dictionary will be deleted

### MW Graph.py
1. Follow CLI to create a graph 

Note: This program will use data from 'MW Daily.py' only 


## Contributions
This will probably be obsolete in a couple years so any pull requests or forks are welcome. 
