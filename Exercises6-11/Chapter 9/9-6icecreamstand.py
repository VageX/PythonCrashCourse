"""A class that can be used to represent a restaurant."""


class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints the name and cuisine type of the restaurant."""
        print("\nName: " + str.title(self.restaurant_name) + ".")
        print("\nCuisine Type: " + str.title(self.cuisine_type) + ".")

    def open_restaurant(self):
        """Prints a message indicating the restaurant is open."""
        print("\n" + str.title(self.restaurant_name) + " is now open.")


class IceCreamStand(Restaurant):

    def __init__(self, *flavors):
        self.flavors = flavors

    def display_flavors(self):
        print("\nFlavors are: " + str(self.flavors))

mr_softie = Restaurant('mr. softie', 'ice cream')
mr_softie.describe_restaurant()

mr_softie = IceCreamStand('vanilla', 'chocolate')
mr_softie.display_flavors()
