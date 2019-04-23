"""Make a class named 'User' with several attributes"""

class User():

    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.full_name = str.title(self.first_name) + " " + str.title(self.last_name)

    def describe_user(self):
        print("\nFirst Name: " + str.title(self.first_name))
        print("Last Name: " + str.title(self.last_name))
        print("Age: " + str(self.age))
        print("Gender: " + str.title(self.gender))

    def greet_user(self):
        print("\nWelcome " + str.title(self.full_name) + " to the program!")

class Admin(User):

    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)
        self.privileges = []

    def show_privileges(self):
        print("\nPrivileges:")
        for privilege in self.privileges:
            print("- " + privilege)

george = Admin('george', 'carty', '31', 'male')
george.describe_user()

george.privileges = [
    'can add post',
    'can delete post',
    'can ban user'
    ]

george.show_privileges()