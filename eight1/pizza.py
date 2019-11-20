def make_pizza(size, *toppings):
    """打印顾客所有的配料"""
    print("the size is " + str(size))
    for topping in toppings:
        print(topping)
