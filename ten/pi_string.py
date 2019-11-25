filename = 'E:\py/ten\source\pi_million_dights.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.rstrip()
    birthday = input("please input your birthday: ")

    if birthday in pi_string:
        print("good luck ")
    else:
        print("sorry")