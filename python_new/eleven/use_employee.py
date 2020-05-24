from python_new.eleven import Employee

my_employee = Employee('xu', 'yulin')


my_employee.show_salary()



while True:
    print("please input 'q' to quit")

    my_salary = input("please input salary :")

    if my_salary == 'q':
        break
    else:
        my_employee.give_raise(int(my_salary))

print("Think you ")

my_employee.show_salary()