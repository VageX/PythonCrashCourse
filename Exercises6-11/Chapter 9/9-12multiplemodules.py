from admin import Admin, Privileges

george = Admin('george', 'carty', '31', 'male')
george.describe_user()
george.privileges.show_privileges()