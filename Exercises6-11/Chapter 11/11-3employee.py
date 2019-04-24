import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.george = Employee('george', 'carty', 60000)

    def test_give_default_raise(self):
        self.george.give_raise()
        self.assertEqual(self.george.salary, 65000)

    def test_give_custom_raise(self):
        self.george.give_raise(10000)
        self.assertEqual(self.george.salary, 70000)

