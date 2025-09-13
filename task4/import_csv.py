import mysql.connector
import csv

con = mysql.connector.connect(
    host="localhost",
    user="prajwal",
    password="Fevicol!1",
    database="movies_db"
)

cursor = con.cursor()
def safe_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def safe_float(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return None

with open('movies.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute("""
            INSERT INTO movies(
                Series_Title, Released_Year, Genre, IMDB_Rating, Director, Star1, Star2, Star3)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            row['Series_Title'],
            safe_int(row['Released_Year']),
            row['Genre'],
            safe_float(row['IMDB_Rating']),
            row['Director'],
            row['Star1'],
            row['Star2'],
            row['Star3'],
        ))

con.commit()
cursor.close()
con.close()

