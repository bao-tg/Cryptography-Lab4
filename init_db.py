import sqlite3

# Connect or create database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create 'users' table
cursor.execute('''
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# Insert default user
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('admin', 'admin123'))

# Add a few more toy users
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('alice', 'pass123'))
cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", ('bob', 'bobpass'))


# Create products table
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    price REAL,
    stock INTEGER
)
''')

# Insert toy product data
cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", ('Apple', 0.5, 100))
cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", ('Banana', 0.3, 150))
cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", ('Chocolate', 1.2, 50))
cursor.execute("INSERT INTO products (name, price, stock) VALUES (?, ?, ?)", ('Water Bottle', 0.8, 75))

conn.commit()
conn.close()

print("Database created with sample users.")
