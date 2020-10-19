import os
from openpyxl import Workbook

try: os.mkdir("Daily"); print("Created: Daily")
except FileExistsError: print("FileExistsError: 'Daily'") # Tries to make Daily folder
try: f = open("Daily//DailyDictStore.txt","x"); f.write("{}"); f.close(); print("    Created: DailyDictStore.txt")
except FileExistsError: print("    FileExistsError: 'DailyDictStore'") # Tries to make daily log
print()

try: os.makedirs("Weekly//LOG"); print("Created: Weekly")
except FileExistsError: print("FileExistsError: 'Weekly//LOG'") # Tries to make weekly folder
try: f = open("Weekly//LOG//Week 0.txt","x"); f.write("[[0]]"); f.close(); print("    Created: Week 0.txt")
except FileExistsError:  print("    FileExistsError: 'Week 0.txt'") # Tries to make weekly log
try: wb = Workbook(); wb.save(filename =f"{os.getcwd()}\\Weekly\\Weekly Spreadsheet.xlsx"); print("    Created: Weekly Spreadsheet.xlsx")
except FileExistsError:  print("    FileExistsError: 'Weekly Spreadsheet.xlsx'") # Tries to make weekly log

# EDIT BELOW
URL1 = "https://www.marketwatch.com/game/padzikintrocohortb/rankings"
# EDIT ABOVE
