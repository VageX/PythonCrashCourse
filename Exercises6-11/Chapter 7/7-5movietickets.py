prompt = "How old are you?"
prompt += "(Press 'q' to quit at any time.) "

active = True
while active:
    age = input(prompt)
    age = int(age)
    if age < 3:
        print("Your ticket is free.")
    elif age < 13:
        print("Your ticket costs $10.")
    elif age >= 13:
        print("Your ticket costs $15.")

