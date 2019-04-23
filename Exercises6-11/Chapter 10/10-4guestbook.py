filename = 'guest_book.txt'

with open(filename, 'a') as file_object:
    active = True
    while active:
        guestbook = input("Please enter your name: ")
        if guestbook == 'q':
            active = False
        else:
            file_object.write(guestbook)
            file_object.write("\n")
            print("Thank you for signing the guestbook " + guestbook.title() + ".")