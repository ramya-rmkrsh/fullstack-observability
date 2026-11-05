import mysql.connector

conn = mysql.connector.connect(
     host=os.environ.get("DB_HOST"),
     database=os.environ.get("DB_NAME"),
     user=os.environ.get("DB_USER"),
     password=os.environ.get("DB_PASSWORD")
)

print("DB connection established")
cursor = conn.cursor()
cursor.execute("SHOW TABLES;")
print(cursor.fetchall())
print("Query executed")
cursor.close()
conn.close()
