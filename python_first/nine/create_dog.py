# import nine.dog as dog
from python_first.nine.dog import *
new_dog = Dog("luming", 17)

print("my dog name is : " + new_dog.name)
print("my dog age is : " + str(new_dog.age))

new_dog.sit()
new_dog.roll_over()

