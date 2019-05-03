from pprint import pprint
import psycopg2

from relational_database.config import DATABASE

conn = psycopg2.connect(**DATABASE)

with conn.cursor() as cursor:


    cursor.execute("SELECT * FROM Customers ORDER BY CustomerID DESC")
    pprint(cursor.fetchall())
