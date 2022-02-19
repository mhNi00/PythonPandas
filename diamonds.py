from asyncio.windows_events import NULL
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
pd.options.display.max_rows = 53940
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
i = True

def caratSpecific(x):
    diamondList = []
    for d in diamonds.carat:
        if d == x:
            diamondList.append(True)
        else:
            diamondList.append(False)
    cut = ''
    for i in range(len(diamondList)):
        if diamondList[i] == True:
            cut += diamonds._get_value(i,'cut') + ','
    print('Carat',x,'cut:',cut)

def exportExcel(): #Export do excela, w przyszlosci dodac wybor kolumn do exportu zadanych w stringu przez uzytkownika
    dataFrame = diamonds.reindex(columns=['carat','table'])
    dataFrame.to_excel('test.xlsx', index=False)

def firstRows(x):
    print("")
    print(diamonds.head(x))

def lastRows(x):
    print("")
    print(diamonds.tail(x))

def basicInfo():
    print("")
    print(diamonds.info())

def priceRange():
    x = diamonds['price'].min()
    y = diamonds['price'].max()
    print("The prices range from",x, "up to",y,".")

def specificDiamond():
    diamondList = []
    while True:
        try:
            minCarat = float(input("Carat range (0.20-5.01) from: "))
            maxCarat = float(input("up to "))
        except ValueError:
            print("You need to enter a number!")
            continue
        break
    for d in diamonds.carat:
        if d >= minCarat and d <= maxCarat:
            diamondList.append(True)
        else:
            diamondList.append(False)
    j = 0
    for i in range(len(diamonds)):
        if j == 0 and diamondList[i] == True:
            print(diamonds.loc[[i]])
            j+=1
        if diamondList[i] == True:
            rows = diamonds.loc[[i]]
            print(rows.to_string(header = False))
    if True not in diamondList:
        print("There's no diamonds in that carat range!")

def makePlot():
    information = diamonds.groupby('cut', as_index=False)['price'].mean()
    xpoints = np.array(information['cut'])
    ypoints = np.array(information['price'])
    print(ypoints)
    print(xpoints)
    plt.plot(xpoints,ypoints, marker='o')
    plt.xlabel("Cut")
    plt.ylabel("Price")
    plt.title("Cut to average price")
    plt.show()

while i == True:
    n = 99
    print("""What would you like to do with the data?
    0. Print out all rows (might take up to a minute!),
    1. Print first x rows of data,
    2. Print last x rows of data,
    3. Print information about the data,
    4. Print out information for diamonds in specific carat range,
    5. Print information about price ranges,
    6. Print a plot showing cut to average price,
    7. Generate statistics,
    8. Export carat and table columns to xlsx file,
    9. Print all cuts with specific carat number seperated by commas,
    10. Exit the program.
                                     """)
    try:
        n = int(input("Choose: "))
    except:
        print("Wrong input, try again")
    print("")
    if n == 0:
        print(diamonds)
    if n == 1:
        while True:
            try:
                x = int(input("How many first rows of data would you like to see? "))
            except:
                print("Wrong input, try again")
                continue
            break
        firstRows(x)
    if n == 2:
        while True:
            try:
                x = int(input("How many last rows of data would you like to see? "))
            except:
                print("Wrong input, try again")
                continue
            break
        lastRows(x)
    if n == 3:
        basicInfo()
    if n == 4:
        specificDiamond()
    if n == 5:
        priceRange()
    if n == 6:
        makePlot()
    if n == 7:
        print(diamonds.describe())
    if n == 8:
        exportExcel()
    if n == 9:
        while True:
            try:
                x = float(input("What carat information would you like to see? "))
            except:
                print("Wrong input, try again")
                continue
            break
        caratSpecific(x)
    if n == 10:
        print("Goodbye :>")
        i = False
    print("")

