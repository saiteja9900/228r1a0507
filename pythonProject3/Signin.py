from tkinter import *
from PIL import ImageTk
import mysql.connector


def saveData():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="saiteja@7259",
        database="customerdata"
    )

    mycursor = conn.cursor()
    sql = "INSERT INTO studentreg (username, email, password) VALUES (%s, %s, %s)"


    username_value = usernameEntry.get()
    email_value = emailEntry.get()
    password_value = passwordEntry.get()


    mycursor.execute(sql, (username_value, email_value, password_value))

    conn.commit()



window = Tk()

background = ImageTk.PhotoImage(file='baby.jpg')
blabel = Label(window, image=background)
blabel.grid()


frame = Frame(window)
frame.place(x=600, y=100)


usernameLabel = Label(frame, text="Username", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
usernameLabel.grid(row=0, column=0, padx=10, pady=5)

usernameEntry = Entry(frame, width=30)
usernameEntry.grid(row=0, column=1)

emailLabel = Label(frame, text="Email", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
emailLabel.grid(row=1, column=0)

emailEntry = Entry(frame, width=30)
emailEntry.grid(row=1, column=1)

passwordLabel = Label(frame, text="Password", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
passwordLabel.grid(row=2, column=0, padx=10, pady=5)

passwordEntry = Entry(frame, width=30)
passwordEntry.grid(row=2, column=1)

submitButton = Button(frame, text="Submit", command=saveData)
submitButton.grid(row=3, column=0, columnspan=2)


window.mainloop()
