import sqlite3
import pandas as pd

def selectData():
    with sqlite3.connect('DBGeneration/superheroes.db') as connection:
        cur = connection.cursor()
        columnsList = []
        cur.execute("PRAGMA table_info(superhero)") # Get column names
        columns = cur.fetchall()
        for column in columns:
            columnsList.append(column[1])
        cur.execute("SELECT * FROM superhero")
        data = cur.fetchall()
    return data, columnsList

def convertToCSV(data, columnsList):
    df = pd.DataFrame(data, columns=columnsList)
    df.to_csv("superheroes.csv", index=False)
    print("Data converted to CSV successfully!")
    return

data, columnsList = selectData()
convertToCSV(data, columnsList)