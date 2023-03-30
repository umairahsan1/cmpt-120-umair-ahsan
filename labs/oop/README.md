# Lab 6 - Object-Oriented Programming

The use of class definitions and objects in Python are good way to reduce code duplication, increase program modularity, and make it easier to debug and solve errors. The goal of this lab is to get you comfortable with defining and using classes.

## Step 1 - Setup

The first thing I want you to do is to create a new folder in the `labs` folder called `oop`. In that folder I want you create the following files: `course.py`, `person.py`, `student.py`, and `test_oop.py`. Copy the contents of `person.py` and `test_oop.py` on my Github to your local versions. Remember to save your files!

## Step 2 - Defining the Course class

The first piece of code I want you to develop is the Course class. In `course.py` I want you to define a class called `Course` that has the following properties: `name`, `number`, `credits`, and `grade`. This class **encapsulates** data related to college courses.

## Step 3 - Defining the Student class

The second piece of code I want you to develop is the `Student` class. This class extends the `Person` class and in addition to the attributess it has inherited it also has the following attributes:

- `major`: a string representing the student's major.
- `courses`: a list of the previously defined Course object.
- `change_major`: a function that reassigns the `major` property
- `get_credits`: a function that iterates through `courses` and returns the total number of credits.
- `get_gpa`: a function that iterates through `courses` and returns the total student's GPA. Use the following dictionary for the letter grade point scale:

```py
grade_map = {
    "A"  : 4.0,
    "A-" : 3.7,
    "B+" : 3.3,
    "B"  : 3.0,
    "B-" : 2.7,
    "C+" : 2.3,
    "C"  : 2.0,
    "C-" : 1.7,
    "D+" : 1.3,
    "D"  : 1.0,
    "F"  : 0.0
}
```

> Note: to calculate the GPA of a student you must multiply number of credit hours a course has by the grade on a 4.0 scale. So two 3 credit courses with a grade of A (4.0) would be 24.0 total points. If you divide the total number of points by the total number of credits you get their GPA. So `24.0 / 6 == 4.0`.

## Step 4 - Unit tests

Finally I want you to run the unit tests to ensure the code is in working order. Activate your python virtual environment and run `pytest`. Please copy and paste the output to the assignment on iLearn and submit it for credit.
