# Lab 3 - File Operations

The goal of this lab is for you familiarize yourself with creating variables, importing libraries, writing to a file, and reading from a file by creating a logger utility. A logger is an important tool for applications of all size and scope. If implemented and used properly it allows you to see what has happened and in what order.

## Step 1 - Copy files to your repository

If you visit https://github.com/kevtr0n-marist/cmpt-120/tree/main/labs/logging you will see the lab instructions as well as some code you need to get started.

If you have done your project setup properly, your repository will be in the following place:

```sh
# on Windows
C:\Users\{uname}\Projects\cmpt-120-{firstname}-{lastname}

# on Mac
/Users/{uname}/Projects/cmpt-120-{firstname}-{lastname}

# on linux
/home/{uname}/Projects/cmpt-120-{firstname}-{lastname}
```

Open up that folder in Visual Studio Code and I want you to create a new folder called `logging` under the `labs` folder. So it should look like this:

```sh
# on Windows
C:\Users\{uname}\Projects\cmpt-120-{firstname}-{lastname}\labs\logging\

# on Mac
/Users/{uname}/Projects/cmpt-120-{firstname}-{lastname}/labs/logging/

# on linux
/home/{uname}/Projects/cmpt-120-{firstname}-{lastname}/labs/logging/
```

In that folder I want you to create 3 files and copy the [code](https://github.com/kevtr0n-marist/cmpt-120/tree/main/labs/logger) I have in the files herw:

- `logger.py`
- `main.py`
- `test_logger.py`

The `logger.py` file will contain our functions for reading/writing to the log file. The `main.py` file will call the code in the `logger.py` file. The `test_logger.py` file contains our unit tests that make sure our code is working properly.

## Step 2 - Naming our log file programmatically

When naming log files, it is customary to include the current date in the name of the log file. So for the first part of the assignment, I want you to programmatically include the current date in the log file name. The log file should have the format `log-file-yyyy-mm-dd.log`. Using the `datetime` package and string concatenation (or interpolation), I want you to reassign the value of `log_file` to include the date.

For help getting the proper date, you may use the [Python Docs](https://docs.python.org/3/library/datetime.html) online or review this [Stack Overflow](https://stackoverflow.com/questions/32490629/getting-todays-date-in-yyyy-mm-dd-in-python) answer.

```py
# Change this to be log-file-yyyy-mm-dd.log
log_file = "log-file.log
```

To import the module, use the proper syntax like so:

```py
from datetime import datetime
```

> Be sure to import the module at the very top of your file!
>
> ~ Kev

## Step 3 - Implement our log function

Next, we want to implement our `log` function in `logger.py`. Refer to our notes in chapter 5 on reading/writing to and from a file. We want to use the built in Python function `open` to open a file and use the proper mode to write to it. Some small caveats is that you will need to manually insert a newline character `\r` at the end of any text you want to log as that is not done for free using the `write` function. When you use this function you will notice a file is created with the text you passed in. However, there is a problem. We do not know when these logs were created!

Next, we want to add a timestamp at the beginning of our logs. Using string concatenation or interpolation, I want you to insert the current date and time at the beginning of the log in the following format:

```sh
[yyyy-mm-dd hh:mm:ss] <text>\n
```

You may refer to the chapter 5 slides as well as same Python docs/Stack Overflow post from step 2 for help.

## Step 4 - Implement our dump function

Next, we want to implement our `dump` function in `logger.py`. Refer to our notes in chapter 5 or the online Python documentation on how to read a file's contexts into a variable. All this function is supposed to do is read the contents of the file into a variable and print that variable out to the user.

## Step 5 - Update our .gitignore

Finally, we are now going to want to update our `.gitignore` file so that our log files are not uploaded to Github every time we push. We can achieve this by adding `*.log` at the end of the file.

## Step 6 - Test our functions

To test our function we are going to run the `pytest` command which will run the new unit tests I have submitted with this assignment. The unit tests will test to make sure that your log file name is the correct format `log-file-yyyy-mm-dd.log`. It will test that it can properly write to and read from the log file. You can also run the `main.py` program I made and watch the logs get created in real time.

## Final Step - Submitting your work

Once you have completed the work for the lab and you test down (all of your unit tests pass). I want you to copy the output of `pytest` and submit it on iLearn.
