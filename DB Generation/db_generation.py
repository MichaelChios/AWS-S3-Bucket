import sqlite3

def create_db():
    with sqlite3.connect("superheroes.db") as connection:
        with open("sqlite.sql", "r") as file:
            sql = ""
            for row in file:
                sql += row
            sql = sql.split(";")
        for query in sql:
            cur = connection.cursor()
            cur.execute(query)

create_db()