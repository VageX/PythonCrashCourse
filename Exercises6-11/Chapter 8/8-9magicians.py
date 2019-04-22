def show_magicians(names):
    """Print each magician on the list."""

    for name in names:
        msg = name.title() + " is a magician."
        print(msg)

magicians = ['george', 'lauren', 'biscuit']
show_magicians(magicians)