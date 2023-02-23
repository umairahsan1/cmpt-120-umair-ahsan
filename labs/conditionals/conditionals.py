'''
Lab 5 - Conditionals and Decision Trees

Syntax for single decision:

if <condition> :
    <body>
    
Syntax for 2-way decision:

if <condition> :
    <body>
else:
    <body>

Syntax for Multi-way decision:

if <condition> :
    <body>
elif <condition> :
    <body>
else:
    <body>
'''


def is_equilateral(x: int, y: int, z: int) -> bool:
    if x == None or y == None or z == None:
        raise Exception("x, y, or z may be 'None'")
    if x == y and y == z:
        return True
    return False


def get_vowels(sentence):
    if sentence is None:
        raise Exception("'sentence' may not be None!")
    vowels = "aeiou"
    results = []
    for i in sentence:
        if i in vowels:
            results.append(i)
    return results


def validate_list(l):
    if type(l).__name__ != 'list':
        raise Exception("!!!")
    if len(l) == 0:
        raise Exception("!!!")
    for i in l:
        if type(i).__name__ != 'int':
            raise Exception("!!!")
    return l


def is_palindrome(text):
    return text == text[::-1]


def calculate_letter_grade(grades):

    if len(grades) == 0:
        raise Exception("!!!")
    if type(grades).__name__ != "list":
        raise Exception("!!!")
    for i in grades:
        if i < 0 or i > 100:
            raise Exception("!!!!")

    average = 0
    total = 0
    for i in grades:
        total += i
    average = total / len(grades)

    if average > 93:
        return "A"
    elif average >= 90:
        return "A-"
    elif average >= 87:
        return "B+"
    elif average >= 83:
        return "B"
    elif average >= 80:
        return "B-"
    elif average >= 77:
        return "C+"
    elif average >= 73:
        return "C"
    elif average >= 70:
        return "C-"
    elif average >= 67:
        return "D+"
    elif average >= 63:
        return "D"
    elif average >= 60:
        return "D-"
    else:
        return "F"
