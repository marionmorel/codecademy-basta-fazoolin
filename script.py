#------------------------------
# Making the Menus
#------------------------------

# Create a Menu class
class Menu:
    # Give Menu a constructor with the five parameters self, name, items, start_time, and end_time
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    
    # Create string representation method
    def __repr__(self):
        return f"{self.name} menu available from {self.start_time} to {self.end_time}"

    # Create a calculate_bill method
    def calculate_bill(self, purchased_items):
        bill = 0
        for item in purchased_items:
            if item in self.items:
               bill += self.items[item]
        return bill

# Create brunch menu
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch = Menu("brunch", brunch_items, 1100, 1600)

# Create early bird menu
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

early_bird = Menu("early bird", early_bird_items, 1500, 1800)

# Create dinner menu
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner = Menu("dinner", dinner_items, 1700, 2300)

# Create kids menu
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids = Menu("kids", kids_items, 1100, 2100)

# Test string representation method on brunch
print(brunch)

# Test calculate.bill() on brunch and early bird menus
print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))
print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))

#------------------------------
# Creating the Franchises
#------------------------------

# Create a Franchise class
class Franchise: 
    # Give the class a constructor that takes the three arguments self, address and menus
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    
    # String representation method to print the address
    def __repr__(self):
        return f"{self.address}"
    
    # Method that tells the customers what menus are available given a time
    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if menu.start_time <= time and time <= menu.end_time:
                available_menus.append(menu)
        return available_menus

# Create two franchises
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

# Test available_menus()
print(flagship_store.available_menus(1200))
print(flagship_store.available_menus(1700))

#------------------------------
# Creating Businesses!
#------------------------------

# Define a Business class
class Business: 
    # Give the class a constructor that takes in the three arguments self, name and franchise
    def __init__(self, name, franchises):
        self.name = name
        self.franchise = franchises
    
# Create a Business instance
basta_fazoolin = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

# Create arepa menu
arepa_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepa_menu = Menu("Take a' Arepa", arepa_items, 1000, 2000)

# Create arepa franchise
arepas_place = Franchise("189 Fitzgerald Avenue", [arepa_menu])

# Create Take a' Arepa business
arepa = Business("Take a' Arepa", [arepas_place])