import pandas as pd
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

while i == True:
    n = 0
    print("""What would you like to do with the data?
    1. Print first x rows of data.
    2. Print last x rows of data.
    3. Print information about the data.
    5. Exit the program.

                                        """)
    n = int(input("Choose: "))
    print("")
    if n == 1:
        x = int(input("How many first rows of data would you like to see? "))
        firstRows(x)
    if n == 2:
        x = int(input("How many last rows of data would you like to see? "))
        lastRows(x)
    if n == 3:
        basicInfo()
    if n == 5:
        print("Goodbye :>")
        i = False
    print("")

