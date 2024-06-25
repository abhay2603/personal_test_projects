import sqlite3

# Connect to SQLite database (creates the database if it doesn't exist)
conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

# Create sales table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    date TEXT,
    product TEXT,
    region TEXT,
    sales INTEGER
)
''')

# Insert sample data
cursor.executemany('''
INSERT INTO sales (date, product, region, sales) VALUES (?, ?, ?, ?)
''', [
    ('2023-01-01', 'A', 'North', 100),
    ('2023-01-02', 'B', 'South', 200),
    ('2023-01-03', 'C', 'East', 150),
    ('2023-01-04', 'D', 'West', 250)
])

# Commit and close connection
conn.commit()
conn.close()

print("Database created and populated successfully.")
