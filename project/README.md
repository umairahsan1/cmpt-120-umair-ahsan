# Project - Server Side Application for Movie Ratings

For our semester long project. We will be working in groups of 2 (or 3 depending on the number of students in the class). Before we start developing the project, we need to understand at very high level was a REST API is. Ironically, REST APIs are not something new. It has been around since the year 2000 but has been very popular recently with the rise of JavaScript libraries. If you are curious about all the specific details, I’ll let you go ahead and read about it on Google as I am not trying to bore you with all these crazy details.

RESTful API stands for **Re**presentational **S**tate **T**ransfer **A**pplication **P**rogramming **I**nterface. At a very high level, RESTful APIs are a way for developers to pass data back and forth to and from a server for an application. It uses the concept of CRUD (Create, Read, Update, Delete). CRUD operations are performed on a piece of data inside of a database but with REST APIs we use the verbs POST, GET, PUT, and DELETE instead.

## Step 1: Groups

First thing to do is to get into groups of 2. This will be your partner for the remainder of the semester. If there is an odd number; there will be **ONE (1) group of three**. Once you have chose your partner, let me know and I will document it in my notes.

## Step 2: Ensuring Flask is installed

First we are going to check and make sure Flask is installed in our python virtual environment. Flask is a micro web framework that allows us to create endpoints inside of Python. It has other functionality, but we only care about the REST APIs here. There are other frameworks out there that allow us to achieve this same functionality, but Flask is a pretty popular framework so we will be working with it in this lab.

Now ensure that your Python3 virtual environment is activated.

1. For Mac/Linux

   ```sh
   # when cd'd into the root folder of your repository.
   source venv/bin/activate
   ```

2. For Windows
   ```sh
    # when cd'd into the root folder of your repository.
    .\venv\Scripts\activate.bat
   ```
   And once it is activated; run the following command to actually install `flask` onto your python virtual environment.

```sh
# check that it is installed properly by running the following command.
flask --version
```

If the command works skip onto step 3. If the command failed the next step is to install Flask. 

Add the following lines to your `requirements.txt` file in your root folder of your repositories.

```py
# the flask package is a tool for creating RESTful interfaces.
flask==2.2.2
```

Next, ensure that your Python3 virtual environment is activated.

1. For Mac/Linux

   ```sh
   # when cd'd into the root folder of your repository.
   source venv/bin/activate
   ```

2. For Windows
   ```sh
   # when cd'd into the root folder of your repository.
   .\venv\Scripts\activate.bat
   ```

And once it is activated; run the following command to actually install `flask` onto your python virtual environment.

```sh
# this makes the flask package available to you when your environment is active.
pip install -r requirements.txt

# check that it is installed properly by running the following command.
flask --version
```

## Step 3: Analyzing/Running the Flask Application

So now that we have Flask installed on our virtual environments. We will now create a new folder in our root folder of our repository called `project`. In that folder I want you to create a new file called `main.py`. In this file I want you to paste the following code inside.

```py
# import the flask package for making rest apis.
from flask import Flask

# create an instance of a Flask object.
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello_world():
    '''
    This is our base route. When visited, we get the text "Hello, world!"
    '''
    return "Hello, world!"

# run our application
app.run()
```

There is some code here that I don't expect you to understand right away, but I just want to get everything in place so that when we do learn it you will be ready to continue. Next, I want you to start the server. We can do that by running the `main.py` file from the command line.

First `cd` into the `project` folder and then run the `main.py` file with python.

```sh
python main.py
```

When you run this command you will see text that looks something like the following:

```txt
 * Serving Flask app 'main'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

This is indicating that the server has started and is blocking you from using that terminal instance until you quit the application by pressing `Ctrl+C`. Before you quit the application, I want you to visit the following website http://127.0.0.1:5000. When the page loads, you will notice that the text is reading `"Hello, world!"`; the very same text our `hello_world` function we defined earlier is returning. That is because it IS returning it, you have just created a server which is serving your code on the http host `127.0.0.1` port `5000`! I want everyone in the group to take a screenshot of the webpage serving the "Hello, world!" text and submit it on iLearn. After that, I want you all to kill the server by hitting `Ctrl+C`, you should now be able to type commands into the terminal once again. Once you have done this, you are finished with part 1 of the project.
