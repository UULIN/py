class Car:

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        lone_name = str(self.year) + " " + self.make + " " + self.model
        return lone_name.title()

    def read_odometer(self):
        """打印汽车里程信息"""
        print("This car " + str(self.odometer_reading) + "'s miles on it.")
