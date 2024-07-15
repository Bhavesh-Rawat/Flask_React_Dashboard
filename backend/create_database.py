import sqlite3
import json

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('dishes.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS dishes (
    dishId INTEGER PRIMARY KEY,
    dishName TEXT NOT NULL,
    imageUrl TEXT NOT NULL,
    isPublished BOOLEAN NOT NULL
)
''')

# Load JSON data from the file
with open('dishes.json', 'r') as f:
    dishes = json.load(f)

# Insert data into table
for dish in dishes:
    cursor.execute('''
    INSERT OR REPLACE INTO dishes (dishId, dishName, imageUrl, isPublished) 
    VALUES (?, ?, ?, ?)
    ''', (dish['dishId'], dish['dishName'], dish['imageUrl'], dish['isPublished']))

# Commit changes and close connection
conn.commit()
conn.close()

print("Database created and populated successfully!")
