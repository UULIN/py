from python_new.nine import Car
class ElectricVar(Car):
    """电动汽车的独特之处
        初始化父类的属性，再初始化电动汽车特有的属性
    """

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print("This car does't need gas"+ str(self.gas))


class Battery():
    """第一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size  = 70):
        """初始化电瓶的属性值"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电池容量的信息"""
        print("This car has a " + str(self.battery_size) + "-KWH")

    def get_range(self):
        """打印一条信息，指出电瓶的续航里程"""

        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range  = 270

        message = "This cat can go approximately " + str(range)
        message += " miles on a full charge."
        print(message
              )

