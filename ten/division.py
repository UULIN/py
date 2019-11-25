print("give me two numbers, and I'll divide them;")
print("Enter 'q' to quit ")
while True:
    first_number = input("\n First number: ")
    if first_number == 'q':
        break
    second_number = input("\n Second_number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't input 0")
    else:
        print(answer)