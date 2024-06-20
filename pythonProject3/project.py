import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()

# Use one of the methods to format the path correctly
image_path = r'C:\Users\saite\Pictures\Screenshots\image.png'

try:
    image = Image.open(image_path)
    background = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=background)
    label.pack()
except Exception as e:
    print(f"Error loading image: {e}")

root.mainloop()
