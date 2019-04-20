sandwich_orders = ['chicken parm', 'pastrami', 'blt', 'pastrami', 'bacon and egg', 'pastrami']
finished_sandwiches = []
print("There is no more pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

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
