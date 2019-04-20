multiples = input("Please enter a number. ")
multiples = int(multiples)

if multiples % 10 == 0:
    print(str(multiples) + " is a multiple of 10.")
else:
    print(str(multiples) + " is not a multiple of 10.")