class Car:

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas = 0
    def get_descriptive_name(self):
        lone_name = str(self.year) + " " + self.make + " " + self.model
        return lone_name.title()

    def read_odometer(self):
        """打印汽车里程信息"""
        print("This car " + str(self.odometer_reading) + "'s miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:

            self.odometer_reading = mileage
        else:
            print("you can't roll back an odometer")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

    def fill_gas_tank(self, increment_gas):
        """车油箱"""
        self.gas += increment_gas
        print("car's gas is " + str(self.gas))

