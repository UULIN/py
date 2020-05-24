filename = 'source/pi_digits.txt'
with open(filename) as file_object:
    # contents = file_object.read()
    # for line in file_object:
    #     print(contents)
    #     print(line.rstrip())
    lines = file_object.readlines()

    for line in lines:
        print(line.rstrip())
