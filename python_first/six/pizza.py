# 存储所点pizza的信息
pizza = {
    'crust': 'think',
    'toppings': ['mushrooms', 'extra cheese']
}

# 概述所点的pizza
print("You ordered a " + pizza['crust'] + "the following toppings:")
for topping in pizza['toppings']:
    print("topping is "+ topping)