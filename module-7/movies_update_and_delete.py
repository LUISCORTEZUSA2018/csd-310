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

def show_films(cursor, title):
    # execute an INNER JOIN on all tables
    cursor.execute(
        "SELECT film_name AS Name, "
        "film_director AS Director, "
        "genre_name AS Genre, "
        "studio_name AS 'Studio Name' "
        "FROM film "
        "INNER JOIN genre ON film.genre_id = genre.genre_id "
        "INNER JOIN studio ON film.studio_id = studio.studio_id"
        " ORDER BY film.film_id"
    )

    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    for film in films:
        print(
            "Film Name: {}\n"
            "Director: {}\n"
            "Genre Name ID: {}\n"
            "Studio Name: {}\n".format(
                film[0],
                film[1],
                film[2],
                film[3]
            )
        )

show_films(cursor, "DISPLAYING FILMS")


# Insert a new film
cursor.execute(
    """
    INSERT INTO film
        (film_name, film_releaseDate, film_runtime,
         film_director, studio_id, genre_id)
    VALUES
        (%s, %s, %s, %s, %s, %s)
    """,
    ("Jaws", "1975", 124, "Steven Spielberg", 3, 1)
)

db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

# Update Alien to Horror
cursor.execute(
    """
    UPDATE film
    SET genre_id = %s
    WHERE film_name = %s
    """,
    (1, "Alien")
)

db.commit()

show_films(
    cursor,
    "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror"
)

# Delete Gladiator
cursor.execute(
    """
    DELETE FROM film
    WHERE film_name = %s
    """,
    ("Gladiator",)
)

db.commit()

show_films(
    cursor,
    "DISPLAYING FILMS AFTER DELETE"
)

cursor.close()
db.close()