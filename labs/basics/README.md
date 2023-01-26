# Assignment 2 - Software Developement Basics

## Step 1 - Basic directory traversal using the command line

Usage of the command line or your development OS is an invaluable skill in the work place. We will be using some basic command line tools to traverse our computer's directories, look at the files, and create new files/folders.

### For Windows users

Open up the `Command Prompt` app. When you open your folder you will be in your home directory. This is likely `C:\Users\yourname`. You can see what directory you are currently in by issuing the `pwd` command which stands for **print working directory**.

Lets give that a shot and see what happens! You should see something like this:

```sh
/c/Users/yourname
```

Now let is see what other files and folders are inside this directory. We can achieve this by issuing the `dir` command. This will list all of files and folders in the current directory.

Now, let us change directories. We now want to go into our python project folder which should reside in the **Projects** folder. We can achieve this by issuing the `cd` command which stands for **change directory**. We can do this like so:

```sh
# Relatively from the home folder.
cd Projects\cmpt-120-your-name

# Or from anywhere.
cd C:\Users\yourname\Projects\cmpt-120-your-name
```

Finally let us go back to our home folder. We can do that a few ways.

```sh
# This will send us back 2 directories.
cd ..\..
```

### For Mac/Linux users

Open up the `terminal` app. When you open your folder you will be in your home directory. This is likely `/Users/yourname` or simply `~`. You can see what directory you are currently in by issuing the `pwd` command which stands for **print working directory**.

Let's give that a shot and see what happens! You should see something like this:

```sh
pwd
/Users/yourname
```

Now let us see what other files and folders are inside this directory. We can achieve this by issuing the `ls` command with the `-l` option command. The `ls` command is used for listing and the `-l` option lets us list the files/folders in the **long** format.

Let us give that a shot and see what we find! You should see something like this:

```sh
~ ls -l
drwx------@   8 kevinhayden  staff     256 Nov 11 13:36 Applications
drwx------@  15 kevinhayden  staff     480 Jan 19 14:12 Desktop
drwx------@  53 kevinhayden  staff    1696 Jan 17 17:09 Documents
drwx------@  39 kevinhayden  staff    1248 Jan 23 16:59 Downloads
drwx------@ 109 kevinhayden  staff    3488 Jan 21 22:00 Library
drwx------+   5 kevinhayden  staff     160 Nov 16 14:16 Movies
drwx------+   5 kevinhayden  staff     160 Oct 17  2019 Music
drwx------+  56 kevinhayden  staff    1792 Jun 22  2022 Pictures
drwxr-xr-x    3 kevinhayden  staff      96 Jul  8  2019 Projects
drwxr-xr-x+   4 kevinhayden  staff     128 Jun 25  2019 Public
```

Next, let us change directories. We now want to go into python project folder which resides in our **Projects** folder. We can achieve this by issuing the `cd` command which stands for **change directory**. We can do this like so:

Note: What folders you can traverse are relative to your current folder unless you specify the entire path.

```sh
# From the home folder.
cd Projects/cmpt-120-your-name

# Or from anywhere (the ~ is your home folder).
cd ~/Projects/cmpt-120-your-name
```

Finally let us go back to our home folder. We can do that a few ways.

```sh
# This will send us back 2 directories.
cd ../..

# This will send us to the last directory we we're in.
cd -

# This will send us to the home folder.
cd ~
```

Getting comfortable with these tools are important and will make you a more efficient developer.

## Step 2 - Basics with python

Please complete the functions in `basics.py`. The functions you must complete are `celsius_to_fahrenheit`, `fahrenheit_to_celsius`, `miles_to_kilometers`, and `kilometers_to_miles`.

In order to test your progress, I created a test file for you to use. You can run this file by running the following command:

```sh
python3 /path/to/folder/labs/basics/main.py
```

In order to run the official test cases via `pytest`. Run the following commands inside your `cmpt-120-your-name`:

```sh
# Activate your python environment.
source venv/bin/activate

# Run the test cases.
pytest
```

## Step 3 - Submit your work

In order for you to complete the assignment you must copy the output of your `pytest` output and paste it into the assignment in iLearn. Next, you must upload your code to Github. You can achieve this by running the following commands:

```sh
# Add the files you want to commit.
git add -A

# Commit the files to pushed.
git commit -m "uploading lab 2"

# Push the code to Github.
git push origin main
```
