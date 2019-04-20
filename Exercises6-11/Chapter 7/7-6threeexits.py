prompt = "How old are you?"
prompt += "(Press 'q' to quit at any time.) "

active = True
while active:
    age = input(prompt)
    if str(age) == 'q':
        active = False
    elif int(age) < 3:
        print("Your ticket is free.")
    elif int(age) < 13:
        print("Your ticket costs $10.")
    elif int(age) >= 13:
        print("Your ticket costs $15.")