pizza_types = ['pepperoni', 'bacon', 'chicken']
friend_pizzas = ['pepperoni', 'bacon', 'chicken']
pizza_types.append('extra cheese')
friend_pizzas.append('onions')

print("My favorite pizzas are:")
for pizza in pizza_types:
    print(pizza.title())
print("\t")
print("My friend's favorite pizzas are:")
for friendpizza in friend_pizzas:
    print(friendpizza.title())