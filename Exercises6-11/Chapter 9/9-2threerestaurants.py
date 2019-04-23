"""A class that can be used to represent a restaurant."""

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints the name and cuisine type of the restaurant."""
        print("\nName: " + str.title(self.restaurant_name) + ".")
        print("Cuisine Type: " + str.title(self.cuisine_type) + ".")

    def open_restaurant(self):
        """Prints a message indicating the restaurant is open."""
        print(str.title(self.restaurant_name) + " is now open.")

restaurant_one = Restaurant('houlihans', 'american')
restaurant_one.describe_restaurant()
restaurant_one.open_restaurant()

restaurant_two = Restaurant('pacific spice', 'asian')
restaurant_two.describe_restaurant()
restaurant_two.open_restaurant()

restaurant_three = Restaurant('brick and bones', 'southern')
restaurant_three.describe_restaurant()
restaurant_three.open_restaurant()