filename = 'programming_poll.txt'

with open(filename, 'a') as file_object:
    active = True
    while active:
        ppoll = input("Why do you like programming?: ")
        if ppoll == 'q':
            active = False
        else:
            file_object.write("Guest likes programming because: " + ppoll + ".")
            file_object.write("\n")
            print("Thank you for your response.")