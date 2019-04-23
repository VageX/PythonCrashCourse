from user import User

class Admin(User):

    def __init__(self, first_name, last_name, age, gender):
        super().__init__(first_name, last_name, age, gender)

        self.privileges = Privileges()

class Privileges():

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print("- " + privilege)
        else:
            print("-This user has no privileges.")
