class Employee():
    """雇员信息"""
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.salarys = []

    def show_salary(self):
        """显示年薪"""
        salary1 = 0
        for salary in self.salarys:
            salary1 += salary

        my_employee = self.first.title() + ' ' + self.last.title()
        print(my_employee + "'s salary is " + str(salary1))

    def give_raise(self, up_salary):
        """增加年薪"""
        self.salarys.append(up_salary)


