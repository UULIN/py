requested_toppings = ['mushrooms', 'green papers', 'extra cheese',"1"]
availabe_toppings = ['olives', 'green papers', "pepperoini", 'extra cheese', 'mushrooms']

for requested_topping in requested_toppings:
    if requested_topping in availabe_toppings:
        print("Add " + requested_topping + ".")
    else:
        print("FUCK")
print("\nFinished making your pizza")