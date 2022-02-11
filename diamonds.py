import pandas as pd
pd.options.display.max_rows = 53940
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
i = True

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
while i == True:
    n = 99
    print("""What would you like to do with the data?
    0. Print out all rows (might take up to a minute!),
    1. Print first x rows of data,
    2. Print last x rows of data,
    3. Print information about the data,
    4. Print out information for a specific diamond,
    5. Print information about price ranges,
    6. Exit the program.

                                        """) # 4. todo
    n = int(input("Choose: "))
    print("")
    if n == 0:
        print(diamonds)
    if n == 1:
        x = int(input("How many first rows of data would you like to see? "))
        firstRows(x)
    if n == 2:
        x = int(input("How many last rows of data would you like to see? "))
        lastRows(x)
    if n == 3:
        basicInfo()
    if n == 4:
        pass
    if n == 5:
        priceRange()
    if n == 6:
        print("Goodbye :>")
        i = False
    print("")

