prompt1 = "\n Tell me something: "
prompt1 += "\n Enter 'quit' to exit."

active = True
while active:
    something = input(prompt1)

    if something == 'quit':
        break