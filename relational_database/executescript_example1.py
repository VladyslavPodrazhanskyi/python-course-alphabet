import psycopg2

from relational_database.config import DATABASE

conn = psycopg2.connect(**DATABASE)

with conn.cursor() as cursor:

    cursor.execute("""INSERT INTO Customers VALUES (149, 'Leonardo Di Caprio');; 
                            SELECT COUNT(CustomerID) FROM Customers;""")
    print(cursor.fetchall())

