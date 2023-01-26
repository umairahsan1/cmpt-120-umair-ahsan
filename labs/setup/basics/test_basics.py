'''
Assignment #2:

    Tests the various capabilities of the conversion 
    functions defined in the basics.py file.


@author Kevin Hayden
@date 2023-01-20
@org Marist College - Department of Computing Science
'''

from basics import *


class TestBasics:

    '''
    Testing the celsius_to_fahrenheit function.
    '''

    def test_00(self):
        assert celsius_to_fahrenheit(0.0) == 32.0

    def test_01(self):
        assert celsius_to_fahrenheit(100.0) == 212.0

    def test_02(self):
        assert celsius_to_fahrenheit(112.0) == 233.6

    def test_03(self):
        assert celsius_to_fahrenheit(1000.0) == 1832.0

    def test_04(self):
        assert celsius_to_fahrenheit(200000.0) == 360032.0

    '''
    Testing the fahrenheit_celsius function.
    '''

    def test_05(self):
        assert fahrenheit_to_celsius(32.0) == 0.0

    def test_06(self):
        assert fahrenheit_to_celsius(212.0) == 100.0

    def test_07(self):
        assert fahrenheit_to_celsius(233.6) == 112.0

    def test_08(self):
        assert fahrenheit_to_celsius(1832.0) == 1000.0

    def test_09(self):
        assert fahrenheit_to_celsius(360032.0) == 200000.0

    '''
    Testing the miles_to_kilometers function.
    '''

    def test_0a(self):
        assert round(miles_to_kilometers(1.0), 3) == 1.609

    def test_0b(self):
        assert round(miles_to_kilometers(100.0), 3) == 160.934

    def test_0c(self):
        assert round(miles_to_kilometers(62.1371)) == 100

    def test_0d(self):
        assert miles_to_kilometers(5000.0) == 8046.72

    def test_0e(self):
        assert miles_to_kilometers(1000000.0) == 1609344.0

    '''
    Testing the kilometers_miles function.
    '''

    def test_0f(self):
        assert round(kilometers_to_miles(1.60934)) == 1.0

    def test_10(self):
        assert kilometers_to_miles(160.934) == 99.99975109146

    def test_11(self):
        assert round(kilometers_to_miles(100.0), 3) == 62.137

    def test_12(self):
        assert round(kilometers_to_miles(8046.72)) == 5000.0

    def test_13(self):
        assert round(kilometers_to_miles(1609344.0)) == 1000000