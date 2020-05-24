import unittest
from python_new.eleven import Employee


class Test_employee(unittest.TestCase):
    """针对employee进行测试"""

    def setUp(self):
        self.employee = Employee('xu', 'yu')
        self.salarys = ['1000', '2000']

    def test_give_custom_raise(self):
        self.employee.give_raise(self.salarys[0])
        self.assertIn(self.salarys[0], self.employee.salarys)

    def test_give_default_raise(self):
        for salary in self.salarys:
            self.employee.give_raise(salary)
        for salary in self.salarys:
            self.assertIn(salary, self.employee.salarys)
