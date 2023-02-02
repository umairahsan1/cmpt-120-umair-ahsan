# import your libraries here.
import os

# the filepath delimiter for this os. (e.g., windows uses '\' OSX/Linux use '/')
delimiter = "\\" if os.name == "nt" else "/"

# the name of the log file to write to.
log_file = "log-file.txt"  # this should be log-file-yyyy-mm-dd.txt


def log(text, log_file=log_file):
    # open up the log file in the correct mode.
    # create a string that has the current date and time in the beginning of the text.
    # append the text to the end of the file.
    # close the file.
    return None


def dump_logs(log_file=log_file):
    '''
    This function prints out
    '''
    # open up the log file in the correct mode.
    # read the file into a list.
    # iterate through each item in the list and print out the results.
    return None
