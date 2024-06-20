import tkinter as tk
from PIL import Image, ImageTk
import mysql.connector

# Example usage
root = tk.Tk()
background = ImageTk.PhotoImage(file='sai.png')
label = tk.Label(root, image=background)
label.pack()
root.mainloop()
