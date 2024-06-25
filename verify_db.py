import sqlite3

# Connect to the database
conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

# Fetch and print data
cursor.execute('SELECT * FROM sales')
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()
