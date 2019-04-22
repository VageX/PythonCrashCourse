def show_magicians(magicians):
    """Print each magician on the list."""
    for magician in magicians:
        print(magician)

def make_great(modified):
    """Add the phrase 'the Great' to each magician's name."""
    #Build a new list to hold the great magicians.
    great_magicians = []

    # Make each magician great, and add it to great_magicians.
    while magicians:
        magician = magicians.pop()
        great_magician = magician.title() + ' the Great'
        great_magicians.append(great_magician)

    # Add the great magicians back into magicians.
    for great_magician in great_magicians:
        magicians.append(great_magician)

magicians = ['george', 'lauren', 'biscuit']
show_magicians(magicians)

print("\n")
make_great(magicians)
show_magicians(magicians)
