from nine.car import *


new_car = Car('audi', 'a4', 2019)

print(new_car.get_descriptive_name())
new_car.update_odometer(22)
new_car.update_odometer(21)
new_car.read_odometer()

my_used_car = Car('subaru', 'outbak', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.fill_gas_tank(1111)

my_used_car.increment_odometer(100)
my_used_car.read_odometer()