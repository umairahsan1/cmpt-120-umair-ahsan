# Assignment 5 - Conditionals and Decision Trees

## Step 1 - Copy files from my Github

Copy the files from https://github.com/kevtr0n-marist/cmpt-120/tree/main/labs/conditionals to a new folder in your project called `conditionals` in your `labs` folder.

## Step 2 - Write the functions

First, write a new function inside your `conditionals.py` file called `is_equilateral`. This function has 3 parameters; `x`, `y`, and `z`. The goal of this function is to check and see if the 3 lengths of a triangle are the same.

1. This function returns `True` when all three sides equal each other; otherwise the returns `False`.
2. This function raises an exception if `x`, `y`, or `z` are not of type `int`.

Secondly, write another function in the same file called `get_vowels`. This function takes a single parameter called `text`. The goal of this function is to iterate through the `text` and add each vowel in the text to a list variable. Once the text has been completely iterated through, the list is returned to the called.

1. This function returns a list containing every vowel in the `text` argument; duplicates are allowed.
2. This function raises an exception if `text` is not a string.

Thirdly, write another function in the same file called `validate_list` that has a single parameter called `grades`. The goal of this function is to make sure that `grades` is a list and that every item in the list is an integer between 0-100.

1. This function raises an exception if `grades` is not a list.
2. This function raises an exception if `grades` is an empty list.
3. This function raises an exception if any item in the list not an integer.
4. This function raises an exception if any item in the list is below 0 or above 100.
5. This function returns the list passed in.

Fourthly, write another function in the same file called `is_palindrome` that has a single parameter called `text`. The goal of this function is to return true if the `text` argument is a palindrome (the same text forwards and backwards e.g., "racecar").

1. This function raises an exception if `text` is not a string.
2. This function returns `True` if the text is a palindrome; returns `False` otherwise.

Finally, write another function in the same file called `calculate_final_grade` which has a single argument called `grades`. The goal of this function is to calculate the average of each grade passed in and then return an appropriate letter grade.

1. This function uses the `validate_list` function from earlier to validate that the grades argument is a list of integers.
2. This function calculates the average of all the grades in the list.
3. This function returns an appropriate letter grade based on the calculated average. Use an if/elif/else to return the proper letter grade. Use the following criteria:
   - average >= 93 is an A
   - average >= 90 is an A-
   - average >= 87 is a B+
   - average >= 83 is a B
   - average >= 80 is a B-
   - average >= 77 is a C+
   - average >= 73 is a C
   - average >= 70 is a C-
   - average >= 67 is a D+
   - average >= 63 is a D
   - average >= 60 is a D-
   - all other grades are an F

## Step 3 - Test and validate your work

Use the `main.py` file to write and test your code's inputs and outputs. When you are comfortable with it, run the unit tests with `pytest`. In order to submit assignment, submit the `pytest` output into the textbox for the assignment on iLearn.
