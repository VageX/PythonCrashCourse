prompt = ("\nPlease add a pizza topping.")
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print("Adding " + topping.title() + " to pizza.")