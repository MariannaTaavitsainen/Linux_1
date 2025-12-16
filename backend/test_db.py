import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='appuser',
    password='changeme',
    database='appdb'
)
cur = conn.cursor()
cur.execute("SELECT NOW()")
print(cur.fetchone())
conn.close()
