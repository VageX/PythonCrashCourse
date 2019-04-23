from collections import OrderedDict

python_terms = OrderedDict()

python_terms['list'] = 'a collection of items in a particular order'
python_terms['conditional test'] = 'an if statement that can be evaluated as True or False'
python_terms['dictionary'] = 'a collection of key-value items'
python_terms['string'] = 'a series of characters'
python_terms['comment'] = 'allows you to write notes in English within your programs'

for key, value in python_terms.items():
    print("\nA " + key + " is " + value + ".")