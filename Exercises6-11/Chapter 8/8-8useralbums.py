def make_album(artist, album):
    """Return a dictionary containing an artist and album after accepting user input."""
    artist_album = artist + ": " + album
    return artist_album.title()

while True:
    print("\nWhat is the name of the artist?")
    print("(enter 'q' at any time to quit.)")

    enter_artist = input("Artist: ")
    if enter_artist == 'q':
        break

    enter_album = input("Album: ")
    if enter_album == 'q':
        break

    formatted = make_album(enter_artist, enter_album)
    print("\nThe artist and album you selected is: " + formatted + ".")