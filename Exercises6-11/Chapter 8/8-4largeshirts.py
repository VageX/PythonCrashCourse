def make_shirt(text, size='large'):
    """Print a sentence summarizing the size of the shirt and the message printed on it."""
    print("\nThe shirt is a size " + size + ".")
    print("\nThe text on the shirt reads " + text.title() + "!")

make_shirt(text='i love python')
make_shirt(size='medium', text='i love python')
make_shirt(size='small', text='dream theater rocks')