def pets(filenames):
    try:
        with open(filenames) as f_obj:
            for line in f_obj:
                print(line)
    except FileNotFoundError:
        pass


filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    print("\n")
    pets(filename.strip())