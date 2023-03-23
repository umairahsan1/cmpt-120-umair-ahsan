# Lab 4 - Functions and Typing

Python has various primitive data types that are used to represent the data in an application. Consider an online shopping site; the items all have a name, manufacturer, and price which can be represented by strings, floats, and other types. Or consider a video game where you can track your score with an integer. Programming is the means of storing, tracking, and manipulating those pieces of data.

## Step 1 - File and folder creation

Open up your repository in vscode and under the labs folder I want you to create a new folder called `typing`. I want you to then copy the files from my repository over into their respective files/folders.

## Step 2 - Primitive data types and assignment

Look at the file `test_types.py`. There are 6 variable there that I want you to assign values to; `my_int`, `my_float`, `my_str`, `my_bool`, `my_byte`, and `my_list`. Please note that I want you to assign an appropriate value to each variable based on the name. So `my_int` should get a whole number assigned to it, `my_float` should get a decimal value, and so on and so forth.

Assigning a value to a variable is as simple as this:

```py
x = 5
my_var = "abcd"
first_name = "Kevin"
is_tired = True
```

Hopefully you have been keeping up with your readings andknow what these data types are and don't look like this.

![Alt Text](https://i.imgur.com/pnzJTq3.gif)

## Step 3 - Test and make sure that you assigned the correct data types.

You can run the file by navigating to the folder that contains the file using the `cd` command and then run `python3 test_types.py` or pressing the play button in vscode with the file open. This will print out all of the values you assigned. You can also test it by running pytest, our unit testing tool. Activate your python virtual environment `venv` and then run `pytest`. Hopefully all of the tests in the `test_types.py` file pass.

## Step 4 - Moving on.

Once you have completed all of these steps, please go to https://github.com/kevtr0n-marist/cmpt-120/tree/main/labs/functions and complete the steps there.
