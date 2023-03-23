# Project - Server Side Application for Movie Ratings

## Assignment 1 - Setup

For our semester long project. We will be working in groups of 2 (or 3 depending on the number of students in the class). Before we start developing the project, we need to understand at very high level was a REST API is. Ironically, REST APIs are not something new. It has been around since the year 2000 but has been very popular recently with the rise of JavaScript libraries. If you are curious about all the specific details, I’ll let you go ahead and read about it on Google as I am not trying to bore you with all these crazy details.

RESTful API stands for **Re**presentational **S**tate **T**ransfer **A**pplication **P**rogramming **I**nterface. At a very high level, RESTful APIs are a way for developers to pass data back and forth to and from a server for an application. It uses the concept of CRUD (Create, Read, Update, Delete). CRUD operations are performed on a piece of data inside of a database but with REST APIs we use the verbs POST, GET, PUT, and DELETE instead.

### Step 1: Groups

First thing to do is to get into groups of 2. This will be your partner for the remainder of the semester. If there is an odd number; there will be **ONE (1) group of three**. Once you have chose your partner, let me know and I will document it in my notes.

### Step 2: Ensuring Flask is installed

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

Next, we're now going to check to see if Flask is actually installed.

```sh
# check that it is installed properly by running the following command.
flask --version
```

If the command works skip onto step 3. If the command failed the next step is to install Flask.

---

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

### Step 3: Analyzing/Running the Flask Application

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

## Assignment 2 - Extending the Application

The next thing we want to do is add some basic static storage for our server which will hold some dummy data before we set up dynamic storage. Create a new file called `movies.py` in your `project` folder next to `main.py` and in that file add the following list.

```py
movies = [
    {
        "title": "Moana",
        "reviews": [
            {
                "username": "movieluvr123",
                "score": 9.1,
                "review": "A great movie to watch with the kids!"
            }
        ]
    },
    {
        "title": "Frozen",
        "reviews": [
            {
                "username": "thecritic17",
                "score": 9.0,
                "review": "My kids love Elsa! I am tired of that song though."
            },
            {
                "username": "movieluvr123",
                "score": 9.8,
                "review": "Let it goooo, let it GOOO!!!"
            }
        ]
    },
    {
        "title": "Aladdin",
        "reviews": [
            {
                "username": "millenialdude1987",
                "score": 9.9,
                "review": "This movie is a certified banger."
            },
            {
                "username": "disneyFAN2009",
                "score": 6.5,
                "review": "They should remake this with CGI, it looks so old!"
            }
        ]
    },
    {
        "title": "Die Hard",
        "reviews": [
            {
                "username": "millenialdude1987",
                "score": 8.0,
                "review": "Yippykiyay, what a good christmas movie."
            },
            {
                "username": "karensmith",
                "score": 4.0,
                "review": "Why do people think this is a christmas movie?"
            },
            {
                "username": "thecritic17",
                "score": 7.3,
                "review": "A time capsule of 90s action, forever a staple in my rotation of 90s action movies."
            }
        ]
    }
]
```

I now want you to update your imports at the top of `main.py` to now include those movies/reviews. We will be using more things from the `flask` framework so for ease of use just import `*` like so.

```py
from flask import *
from movies import movies
```

### Step 1: Adding a new app route

Now we have to create a new REST endpoint to access these movies. We are going to be doing some exercises with the HTTP method "GET". The GET method is used when you want to let a server know that you want it to response with some specified data that is stored on it. Please copy the following code below and paste it below your `hello_world` function.

```py
@app.route("/api/movies", methods=["GET"])
def list_movies():
    """
    This function returns a Response object back containing all
    of stored movies and reviews back to the caller on the web.
    """
    return jsonify(movies)
```

In the code above, we see a function called `list_movies()` with some weird stuff above it. This is known as an __annotation__. Annotations are a sort of arbitrary marker that exist to notify interpreters, linters, IDEs, etc. about something specific to it. In the case of `flask`, it is notifying the framework that the following function should be invoked when the URL is accessed with a http GET request. I want you to activate your Python virtual environment and then run your `main.py` file. Once again you should see some text like the following:

```txt
 * Serving Flask app 'main'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

I want you to now access the following web page and take a screenshot http://127.0.0.1:5000/api/movies. You should now see a json/dict representation of all of our movie and review data!

### Step 2: Filtering our movie data

So what if want to filter our movie data by certain attributes? Well we can use something called "query parameters" in our URL with the syntax of `{url}?{key}={value}`. So if we want to look at only reviews of the movie "Frozen" we would just go to the URL http://127.0.0.1:5000/api/movies?title=Frozen. Currently if we access that URL we still see all of the movies so let us change that.

### Step 3: Using query parameters

In order to use query parameters we will need to use the `request` object in the `flask` framework. We can access the query parameters in a URI like so:

```py
abcd = request.args.get("abcd")
```

So if someone issues the request http://127.0.0.1:5000?abcd=1234 the `abcd` variable would be assigned `"1234"`. Use a for loop to iterate through each movie in the list and add that movie a list called `response_body`.

```py

@app.route("/api/movies", methods=["GET"])
def list_movies():
    """
    This function returns a Response object back containing all
    of stored movies and reviews back to the caller on the web.

    This function is filterable by a movie title query parameter.
    """
    response_body = movies

    # get the movie title query parameter.
    title = request.args.get("title")

    # only get the movies that have the same title as the query parameter.
    if None not in [title]:
        response_body = [movie for movie in movies if movie["title"] == title]

    return jsonify(response_body)
```

Once this is working, please access http://127.0.0.1:5000?title=Frozen and take a screenshot.

### Step 4: Applying multiple query parameters

So what about if we want to filter by multiple movies? You can apply multiple filters by separating your query parameters by an `&`. For example the following URI http://127.0.0.1:5000/api/movies?title=Frozen&title=Moana can now return a list of query parameters in your endpoint function. To can access them as a list using the following function: `request.args.getlist("title")`. Modify your `list_movies` function to now filter by list of titles.

```py
@app.route("/api/movies", methods=["GET"])
def list_movies():
    """
    This function returns a Response object back containing all
    of stored movies and reviews back to the caller on the web.
    """
    response_body = movies

    titles = request.args.getlist("title")

    # only get the movies that have the same title as the query parameter.
    if titles != []:
        response_body = [movie for movie in movies if movie["title"] in titles]

    return jsonify(response_body)
```

Once this is working, please access http://127.0.0.1:5000?/api/movies/title=Frozen&title=Moana and take a screenshot.

### Step 5: Enabling unit tests

In order to allow for the use of unit testing with pytest, we must encase our `app.run()` call in `main.py` in an if-statement like so:

```py
if __name__ == '__main__':
    app.run()
```

This is required so that when `main.py` is interpreted by the interpreter when using pytest, the app server isn't started.

### Step 6: Running unit tests

Please copy the `test_main.py` file in my projects folder in github to your projects folder and then run:

```sh
pytest test_main.py
```

If everything was done properly, you should get 4 passing tests.

## Step 7: Submitting your work

Please upload the following:

- Screen shot of http://127.0.0.1:5000/api/movies
- Screen shot of http://127.0.0.1:5000/api/movies?title=Frozen
- Screen shot of http://127.0.0.1:5000/api/movies?title=Frozen&title=Moana
- Screen shot of the output of `pytest` command with passing test cases.
