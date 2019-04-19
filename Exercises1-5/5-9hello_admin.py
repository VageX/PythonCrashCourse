usernames = ['darkpandemona83', 'vagex', 'lmyeung90', 'gcarty', 'admin']
if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello " + user.title() + ", would you like to see a status report?")
        elif user in usernames:
            print("Hello " + user.title() + ", thank you for logging in again.")
else:
    print("We need to find some users!")

print("\t")

usernames = []
if usernames:
    for user in usernames:
        if user == 'admin':
            print("Hello " + user.title() + ", would you like to see a status report?")
        elif user in usernames:
            print("Hello " + user.title() + ", thank you for logging in again.")
else:
    print("We need to find some users!")

