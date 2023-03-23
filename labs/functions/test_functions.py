'''
Assignment #4:

    Tests the various capabilities of functions we defined in the functions.py module.


@author Kevin Hayden
@date 2023-02-04
@org Marist College - Department of Computing Science
'''

from functions import *


class TestFunctions:

    def test_00(self):
        '''
        Test 00: ensure that the return value is a string.
        '''
        assert type(join_strings(["a", "b", "c", "d"])).__name__ == "str"

    def test_01(self):
        '''
        Test 01: ensure that the function is returning the correct value.
        '''
        assert join_strings(["a", "b", "c", "d"]) == "abcd"

    def test_02(self):
        '''
        Test 02: ensure that the function isn't hard coded to return the previous value.
        '''
        assert join_strings(["ab", "cd", "ef", "gh"]) == "abcdefgh"

    def test_03(self):
        '''
        Test 03: ensure that the function is returning the correct value.
        '''
        assert mad_libs(
            "Kevin", "math", "Blink 182 show") == "Kevin is too cool for math class. Instead she/he will be attending the Blink 182 show"

    def test_04(self):
        '''
        Test 04: ensure that the function isn't hard coded to return the previous value.
        '''
        assert mad_libs(
            "Jane", "science", "Victoria secret fashion week") == "Jane is too cool for science class. Instead she/he will be attending the Victoria secret fashion week"

    def test_05(self):
        '''
        Test 05: ensure that the caesar_cipher function can encrypt.
        '''
        assert caesar_cipher("hello my name is kevin!",
                             14) == "vszzc am boas wg ysjwb!"

    def test_06(self):
        '''
        Test 06: ensure that the ceasar_cipher function can decrypt as well.
        '''
        assert caesar_cipher("vszzc am boas wg ysjwb!",
                             -14) == "hello my name is kevin!"

    def test_07(self):
        '''
        Test 07: ensure that the inputs and outputs are not hardcoded.
        '''
        assert caesar_cipher("wxyzabcd", -4) == "stuvwxyz"

    def test_08(self):
        '''
        Test 08: ensure that the inputs and outputs are not hardcoded.
        '''
        assert caesar_cipher("stuvwxyz", 4) == "wxyzabcd"
