class FoodDonation:
    def __init__(self):
        self.donor_location = None
        self.donated_food = []

    def set_donor_location(self, location):
        self.donor_location = location

    def donate_food(self, food_item):
        self.donated_food.append( food_item )

    def display_donations(self):
        print( "Donor Location:", self.donor_location )
        print( "Donated Food Items:" )
        for item in self.donated_food:
            print( "-", item )


# Example usage:
donation = FoodDonation()
donation.set_donor_location( "123 Main St, City, Country" )
donation.donate_food( "Canned vegetables" )
donation.donate_food( "Pasta" )
donation.donate_food( "Canned soup" )

donation.display_donations()
