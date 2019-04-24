import unittest
from city_functions import location

class NamesTestCase(unittest.TestCase):

    def test_city_country(self):
        test_one = location('tokyo', 'japan')
        self.assertEqual(test_one, 'Tokyo, Japan')

    def test_city_country_population(self):
        test_two = location('tokyo', 'japan', '5000')
        self.assertEqual(test_two, 'Tokyo, Japan - Population=5000.')

unittest.main()