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
        with open("data.json", "r") as file:
            data = json.load(file)
            for i in range(len(data)):
                id = data[i]["id"]
                name = data[i]["name"]
                description = data[i]["description"]
                power = data[i]["powers"]
                appearance = data[i]["appearances"]
                quote = data[i]["quotes"]
                ally = data[i]["allies"]
                enemy = data[i]["enemies"]
                affiliation = data[i]["affiliation"]
                first_appearance = data[i]["firstAppearance"]
                creator = data[i]["creator"]
                aka = data[i]["aka"]
                cur.execute(
                    f"""INSERT INTO superhero
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""", (id, name, description, power, appearance,
                    quote, ally, enemy, affiliation, first_appearance, creator, aka)
                )
        connection.commit()
    print("Data inserted successfully!")
    return