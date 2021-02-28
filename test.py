import psycopg2
from config import config

# read connection parameters
params = config()

# connect to the PostgreSQL server
print("Connecting to the PostgreSQL database...")
con = psycopg2.connect(**params)

print("Database opened successfully")

# create a cursor
cur = con.cursor()

# run commands using execute
cur.execute("SELECT title from film LIMIT 10")
rows = cur.fetchall()

for row in rows:
    print(row)

# close the connection
print("Done")
con.close()
