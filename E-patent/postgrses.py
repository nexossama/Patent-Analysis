import psycopg2

host="localhost"
database="patent"
user="postgres"
password="postgres"
conn = psycopg2.connect(
    host,
    database,
    user,
    password
)

# Create a cursor object
cur = conn.cursor()