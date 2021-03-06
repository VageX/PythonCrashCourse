import json

filename = 'favorite_number.json'

try:
    with open(filename) as f_obj:
        favorite_number = json.load(f_obj)
        print("I know your favorite number! It's " + str(favorite_number) + ".")
except FileNotFoundError:
    favorite_number = input("What is your favorite number?")
    with open(filename, 'w') as f_obj:
        json.dump(favorite_number, f_obj)
        print("Recording your favorite number.")

