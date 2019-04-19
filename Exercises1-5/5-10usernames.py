current_users = ['darkpandemona83', 'vagex', 'lmyeung90', 'gcarty', 'admin']
new_users = ['tupac', 'biggie', 'darkpandemona83', 'vagex', 'nas']

current_users_lower = [user.lower() for user in current_users]

if new_users:
    for new_user in new_users:
        if new_user.lower() in current_users_lower:
            print("That username is not available.")
        else:
            print("That username is available.")