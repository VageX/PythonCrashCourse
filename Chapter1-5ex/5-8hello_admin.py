usernames = ['darkpandemona83', 'vagex', 'lmyeung90', 'gcarty', 'admin']
for user in usernames:
    if user == 'admin':
        print("Hello " + user.title() + ", would you like to see a status report?")
    else:
        print("Hello " + user.title() + ", thank you for logging in again.")