from bs4 import BeautifulSoup as soup
import requests
from ast import literal_eval
from MWSetup import URL1

try: URL = URL1
except NameError: print("Go into MWSetup and set a URL"); exit()

loPath = "Daily\\DailyDictStore.txt"
dataDict = {}
z = 0

day = int(input("What day is it?: "))
def removeNonAscii(s): return "".join(i for i in s if ord(i)<126 and ord(i)>31) # Imported function to remove formatting

# Get the code of the webpage
def getCode(page): #Input the page of results to get code from
        pageIndex = (page*10)
        gameRankURL = (f'{URL}?partial=true&index={pageIndex}')

        s = requests.session() # Start session
        r = s.get(gameRankURL) # Get code from URL
        code = soup(r.content, 'html.parser') # Parse code for HTML
        return code # Returns HTML of rankings page

# Parse the code for the ranking data
def getTable(code): # Input code of the site
    table = code.find("table",{"class":"table table--primary ranking"}).tbody.findAll("tr",{"class":"table__row"}) # Gets code we want; Table is a list of rows
    return table # Returns the HTML table of the rankings page

# Create an array out of the ranking data
def rank(table,index): # Input HTML table; Input rank index
    row = table[index].findAll("td") # Row is rows of data
    name = removeNonAscii(row[1].text) # Removes formatting
    treturn = float(((row[5].text).replace("$","")).replace(",","")) # Removes the $ sign; Removes the ,; cast into float

    Person = [name,treturn]
    global z
    z += 1
    print(f"    Person added ({z}/{numberPeople})")
    return Person # Returns the statistics of the index

def getRank(page,index): return rank(getTable(getCode(page)),(index-(page*10))) # Simplify a compound of functions into a single one

# Get the number of people in the game
code = getCode(0)
String = code.find("span",{"class":"text align--center"}).text
numberPeople = int(String[18:-8])

f = open(loPath,"r")
dataDict = literal_eval(f.read())
f.close()

# Attach together all of the ranking data into a dictionary
print("Creating dataArray")
for i in range(numberPeople): # Loop for however many people there are
    page = i // 10
    List = getRank(page,i) # Makes a list of name and value

    if List[0] in dataDict:
        dataDict[List[0]].append([day,List[1]])
    else:
        dataDict[List[0]] = [[day,List[1]]]
        print(f"    {List[0]}'s person entry added")
        print("")

print(" ")
print("Cleansing dataArray")

keys = list(dataDict.keys())
for key in keys:
    if dataDict[key][-1][0] != day: # Removes anyone who is no longer in the game
        del dataDict[key]
        print(f"    {key}'s person entry removed")
    else:
        pass
print("")

f = open(loPath,"w")
f.write(str(dataDict))
f.close()

input("Press any key to exit")
