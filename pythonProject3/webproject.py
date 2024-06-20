import tkinter as tk

class FoodDonationApp:
    def __init__(self, master):
        self.master = master
        master.title("Food Donation System")

        self.label = tk.Label(master, text="Enter your location:")
        self.label.pack()

        self.location_entry = tk.Entry(master)
        self.location_entry.pack()

        self.food_label = tk.Label(master, text="Enter donated food items (separated by commas):")
        self.food_label.pack()

        self.food_entry = tk.Entry(master)
        self.food_entry.pack()

        self.donate_button = tk.Button(master, text="Donate", command=self.donate_food)
        self.donate_button.pack()

        self.output_label = tk.Label(master, text="")
        self.output_label.pack()

    def donate_food(self):
        location = self.location_entry.get()
        food_items = self.food_entry.get().split(',')

        self.output_label.config(text="Donor Location: {}\nDonated Food Items: {}".format(location, ", ".join(food_items)))

# Create tkinter window
root = tk.Tk()
app = FoodDonationApp(root)
root.mainloop()
