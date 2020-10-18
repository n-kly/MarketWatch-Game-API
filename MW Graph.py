from ast import literal_eval
from matplotlib import pyplot as plt

loPath = "Daily\\DailyDictStore.txt"
choice = "Hi"

f = open(loPath,"r")
dataDict = literal_eval(f.read())
f.close()

nameList = list(dataDict.keys()) # Sorts array
nameList.sort()

while choice != "00":
    x = []
    y = []
    i = 1
    # Prints out all names in order (Also some neat formatting)
    print("-"*29)
    for name in nameList: print(f"{i:02} : {name}"); i +=1
    print("-"*29)
    print("Type '00' to exit program")
    print("-"*29)
    choice = str(input("Who would you like to graph?: "))
    print()
    print()

    if choice == "00": # Exits if 00
        pass

    else:
        try: # Tries to convert index to dictionary key
            choice = (int(choice) - 1)

            selection = nameList[choice]
            dataList = dataDict[selection]
            for data in dataList:
                x.append(data[0])
                y.append(data[1])

            # Creates graph
            plt.plot(x,y)
            plt.title(f"Graph of {selection}'s returns'")
            plt.ylabel("Return ($)")
            plt.xlabel("Days")
            plt.show()

        except IndexError: # If the index doesnt exist run this error
            print("---------Index Error---------")
            print("----------Try again----------")
            print()
            print()
