sandwich_orders = ['chicken parm', 'blt', 'bacon and egg']
finished_sandwiches = []

while sandwich_orders:
    workinprogress = sandwich_orders.pop()

    print("Making your " + workinprogress.title() + ".")
    finished_sandwiches.append(workinprogress)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    if sandwich == 'blt':
        print(sandwich.upper())
    else:
        print(sandwich.title())
