person = [x for x in range(1,31)]
del_number = 8
for i in range(15):
    print(person[del_number])
    del person[del_number]
    del_number = (del_number + 8) % len(person)