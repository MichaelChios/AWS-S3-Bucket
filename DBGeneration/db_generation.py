import sqlite3
import json

def createDB():
    with sqlite3.connect('DBGeneration/superheroes.db') as connection:
        with open("DBGeneration/sqlite.sql", "r") as file:
            sql = ""
            for row in file:
                sql += row
            sql = sql.split(";")
        for query in sql:
            cur = connection.cursor()
            cur.execute(query)
        connection.commit()
    print("Database created successfully!")
    
def insertData():
    with sqlite3.connect('DBGeneration/superheroes.db') as connection:
        cur = connection.cursor()
        with open("filtered_data.json", "r") as file:
            data = json.load(file)
            for i in range(len(data)):
                id = data[i]["id"]
                name = data[i]["name"]
                description = data[i]["description"]
                power = ','.join(data[i]["powers"])
                quote = ','.join(data[i]["quotes"])
                affiliation = data[i]["affiliation"]
                creator = data[i]["creators"]
                aka = ','.join(data[i]["aka"])
                cur.execute(
                    f"""INSERT INTO superhero
                    VALUES (?,?,?,?,?,?,?,?)""", (id, name, description, power, quote, affiliation, creator, aka)
                )
        connection.commit()
    print("Data inserted successfully!")
    return

def deleteData():
    with sqlite3.connect('DBGeneration/superheroes.db') as connection:
        cur = connection.cursor()
        cur.execute("DELETE FROM superhero")
        connection.commit()
    print("Data deleted successfully!")

# createDB()
# insertData()
# deleteData()