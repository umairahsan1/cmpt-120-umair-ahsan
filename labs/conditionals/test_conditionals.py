'''
Assignment #5:

    Tests the various capabilities of the functions  
    defined in the conditionals.py file.


@author Kevin Hayden
@date 2023-02-11
@org Marist College - Department of Computing Science
'''

from conditionals import *


class TestConditionals:

    def test_00(self):
        '''
        Test that the function returns true when given 3 ints of the same value.
        '''
        assert is_equilateral(1, 1, 1)

    def test_01(self):
        '''
        Test that the function properly returns false when give 3 different int values.
        '''
        assert not is_equilateral(1, 2, 3)

    def test_02(self):
        '''
        Test that the function raises an exception when passed a non-int.
        '''
        try:
            is_equilateral(None, 2, 3)
            assert False
        except Exception:
            assert True

    def test_03(self):
        '''
        Test that the function raises an exception when passed a non-int.
        '''
        try:
            is_equilateral(1, None, 3)
            assert False
        except Exception:
            assert True

    def test_04(self):
        '''
        Test that the function raises an exception when passed a non-int.
        '''
        try:
            is_equilateral(1, 2, None)
            assert False
        except Exception:
            assert True

    def test_05(self):
        '''
        Test that the function raises an exception when passed a non-int.
        '''
        try:
            is_equilateral(None, None, None)
            assert False
        except Exception:
            assert True

    def test_06(self):
        '''
        Test that the function raises an exception when passed a non-int.
        '''
        try:
            is_equilateral('a', 2, 3)
            assert False
        except Exception:
            assert True

    def test_07(self):
        '''
        Test that the function raises an exception when passed a non-int.
        '''
        try:
            assert is_equilateral(1, 'b', 3)
        except Exception:
            assert True

    def test_08(self):
        '''
        Test that the function raises an exception when passed a non-int.
        '''
        try:
            is_equilateral(1, 2, 'c')
            assert False
        except Exception:
            assert True

    def test_06(self):
        '''
        Test that the function returns the vowels in a list.
        '''
        assert get_vowels("Hello world!") == ["e", "o", "o"]

    def test_07(self):
        '''
        Test that the function returns an empty list when handed no vowels.
        '''
        assert get_vowels("CCCCCcccc") == []

    def test_08(self):
        '''
        Test that the function properly raises an exception when passed 'None'.
        '''
        try:
            get_vowels(None) == ['o', 'e']
            assert False
        except Exception:
            assert True

    def test_09(self):
        '''
        Test that the function can properly validate a list of integers.
        '''
        try:
            assert validate_list([1, 2, 3, 4]) == [1, 2, 3, 4]
        except Exception:
            assert False

    def test_0a(self):
        '''
        Test that the function raises an exception when the list contains a non-int.
        '''
        try:
            validate_list([1, 2, 3, None])
            assert False
        except Exception:
            assert True

    def test_0b(self):
        '''
        Test that the function raises an exception when it receives an empty list.
        '''
        try:
            validate_list([])
            assert False
        except Exception:
            assert True

    def test_0c(self):
        '''
        Test that the function raises an exception when it receives a non-list argument.
        '''
        try:
            validate_list("Hello!")
            assert False
        except Exception:
            assert True

    def test_0d(self):
        '''
        Test that function can properly identify palindromes.
        '''
        assert is_palindrome("racecar")

    def test_0e(self):
        '''
        Test that the function can handle palindromes with capital letters.
        '''
        assert is_palindrome("Racecar")

    def test_0f(self):
        '''
        Test that if the function receives a non-palindrome, it returns false.
        '''
        assert not is_palindrome("caesar")

    def test_10(self):
        '''
        Test
        '''
        assert calculate_letter_grade([70, 80, 90, 100, 68, 87, 96, 86]) == "B"

    def test_11(self):
        '''
        Test
        '''
        assert calculate_letter_grade([96, 96, 100]) == "A"

    def test_12(self):
        '''
        Test
        '''
        assert calculate_letter_grade([0]) == "F"

    def test_13(self):
        '''
        Test
        '''
        try:
            grade = calculate_letter_grade([])
        except Exception:
            assert True

    def test_14(self):
        '''
        Test
        '''
        try:
            grade = calculate_letter_grade([101])
            assert False
        except Exception:
            assert True

    def test_15(self):
        '''
        Test
        '''
        try:
            grade = calculate_letter_grade([-30])
            assert False
        except Exception:
            assert True
