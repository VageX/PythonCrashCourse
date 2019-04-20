def make_shirt(size, text):
    """Print a sentence summarizing the size of the shirt and the message printed on it."""
    print("\nThe shirt is a size " + size + ".")
    print("\nThe text on the shirt reads " + text.title() + "!")

make_shirt('large', 'dream theater rocks')

make_shirt(size='medium', text='dream theater rocks')