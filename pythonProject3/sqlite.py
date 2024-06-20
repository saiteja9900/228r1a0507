import sqlite3

# Connect to the database (or create it if it doesn't exist)
con = sqlite3.connect("mydatabase.db")
cur = con.cursor()

# Create the table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    name VARCHAR(50),
    roll_no VARCHAR(50),
    section VARCHAR(50)
)
""")

# Insert data into the table
cur.execute('INSERT INTO students VALUES ("sai", "101", "cse")')
cur.execute('INSERT INTO students VALUES ("asad", "102", "cse")')
cur.execute('INSERT INTO students VALUES ("kevin", "103", "cse")')
cur.execute('delete from students where name="sai" ')
cur.execute('update students set name="sai" where roll_no="103"')

# Select all data from the table
x = cur.execute('SELECT * FROM students')
print(x.fetchall())

# Commit the changes and close the connection
con.commit()
con.close()

