from eleven.name_function import get_formatted_name

print("input 'q' quit")

while True:
    first = input(" \nplease input first name: ")
    if first == 'q':
        break
    last = input(" \nplease input last name: ")
    if last == 'q':
        break
    format_name = get_formatted_name(first, last)
    print("\n full_name is ", format_name)
