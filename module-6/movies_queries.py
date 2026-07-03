import mysql.connector
from dotenv import dotenv_values

secrets = dotenv_values(".env")

db = mysql.connector.connect(
    host=secrets["HOST"],
    user=secrets["USER"],
    password=secrets["PASSWORD"],
    database=secrets["DATABASE"]
)

cursor = db.cursor()

# Query 1
cursor.execute("SELECT * FROM studio")
studios = cursor.fetchall()

print("-- DISPLAYING Studio RECORDS --")
for studio in studios:
    print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

# Query 2
cursor.execute("SELECT * FROM genre")
genres = cursor.fetchall()

print("-- DISPLAYING Genre RECORDS --")
for genre in genres:
    print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

# Query 3
cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
films = cursor.fetchall()

print("-- DISPLAYING Short Film RECORDS --")
for film in films:
    print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))

# Query 4
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
directors = cursor.fetchall()

print("-- DISPLAYING Director RECORDS in Order --")
for director in directors:
    print("Film Name: {}\nDirector: {}\n".format(director[0], director[1]))

cursor.close()
db.close()