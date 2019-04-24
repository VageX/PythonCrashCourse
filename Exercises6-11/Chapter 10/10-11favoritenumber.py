import json

filename = 'favorite_number.json'

favorite_number = input("What is your favorite number?")

with open(filename, 'w') as f_obj:
    json.dump(favorite_number, f_obj)
    print("Recording your favorite number.")



