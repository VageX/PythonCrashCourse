import pizzamodule

pizzamodule.make_pizza(16, 'pepperoni')
pizzamodule.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Or I can import specific functions.

from pizzamodule import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using as to give a function an alias

from pizzamodule import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')