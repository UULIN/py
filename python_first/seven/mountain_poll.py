answers ={}
active = True
while active:
    name = input("please input name: ")
    answers[name] = input("please input answer: ")
    select = input("Would you like continue（YES/NO） ?  ").lower()
    while select == 'yes':
        continue
    while select == 'no':
        print("Think you very much")
        active = False


for name1,answ1 in answers.items():
    print(name1 + "'s answer is " + answ1)