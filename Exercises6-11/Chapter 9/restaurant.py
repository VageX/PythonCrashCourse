"""A class that can be used to represent a restaurant."""

class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints the name and cuisine type of the restaurant."""
        print("\nName: " + str.title(self.restaurant_name) + ".")
        print("\nCuisine Type: " + str.title(self.cuisine_type) + ".")

    def open_restaurant(self):
        """Prints a message indicating the restaurant is open."""
        print("\n" + str.title(self.restaurant_name) + " is now open.")

    def announce_number_served(self):
        print("\n" + str.title(self.restaurant_name) + " served " +
              str(self.number_served) + " people.")

    def set_number_served(self, amount):
        self.number_served = amount

    def increment_number_served(self, people):
        self.number_served += people
