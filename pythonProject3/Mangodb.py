import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="saiteja@7259",
    database="mydb"
)

mycurs = mydb.cursor()
mycurs.execute( "CREATE TABLE users (name VARCHAR(50), email VARCHAR(50), password VARCHAR(50))" )
mycurs.execute( "SHOW TABLES" )
sql = "INSERT INTO users (name, email, password) values(%s,%s,%s)"
val = ("saiteja", "saiteja6130@gmail.com", "tejatej")
mycurs.execute( sql, val )
mydb.commit()  # Don't forget to commit the changes
print( mycurs )