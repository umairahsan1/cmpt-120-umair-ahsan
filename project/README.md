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

In the code above, we see a function called `list_movies()` with some weird stuff above it. This is known as an **annotation**. Annotations are a sort of arbitrary marker that exist to notify interpreters, linters, IDEs, etc. about something specific to it. In the case of `flask`, it is notifying the framework that the following function should be invoked when the URL is accessed with a http GET request. I want you to activate your Python virtual environment and then run your `main.py` file. Once again you should see some text like the following:

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

# Assignment 3 - Completing CRUD Model

So currently we have the ability to retrieve all movies in our collection and apply filters on the list. Now we need to handle the ability to create, update, and delete movies as well as their subsequent reviews.

## Step 1: Setup

At the top of your file, I want you to import the `uuid` library.

```py
import uuid
```

Delete the `movies.py` file that currently contains the test movie data and remove the import from the top of `main.py`. Add the following line **_BELOW_** your app variable initialization.

```py
movies = []
```

Download Postman from https://www.postman.com/; this is the tool we used in class to issue requests against our REST server. In order to use this tool you must sign up with an account. Use the APIs tab on the left. When sending requests that contain a request body you must add the correct headers. Under the "Headers" tab for your request add the following:

| Key          | Value            |
| ------------ | ---------------- |
| Content-Type | application/json |

In order to add your actual request body; under the body tab, select the `raw` radio button and add your dictionary data there.

## Step 2: GET and POST

Let us rename our `list_movies` function to something more appropriate since we are going to be doing more than just listing movies with the function. Let is rename it to `handle_movies`. Let us update our annotation to now include the `POST` method. So your function identifier should now look like:

```py
@app.route("/api/movies", methods=["GET", "POST"])
def handle_movies():
    # GET & POST method logic
```

Now you need to separate your HTTP GET method logic from your HTTP POST method logic. You can do that by accessing what type of request was made using the `request` library like so:

```py
if request.method == "GET":
    # previous GET logic
elif request.method == "POST":
    # new POST logic
```

So under the if-statement checking if it is a GET request; you can just use the list movies logic you previously had. Under the POST request, I want you to retrieve the request body by using the `request.get_json()` function. This will return the HTTP request body as a python dictionary.

```py
request_body = request.get_json()
```

I want you to check for the following error cases:

1. If the request body is `None` or the `title` field in the request body is `null` or in Python `None`; return a `Response("Bad request", 400)`.
2. If the title in the request body matches a movie that already exists in our collection; return a `Response("Already exists.", 409)`.

Once you get past these two error cases. I want you to create a new dictionary object that has a **uuid** field, a **title** field, and a **reviews** field. The uuid you can get from calling `uuid.uuid4()`.

_Make sure you convert the uuid to a string!_

The title you must get from the request body, and the reviews field must be an empty list. Finally, append the dictionary to `movies` and return a `Response("Created", 201)` back to the client.

## Step 3: GET and DELETE by ID

Create a new function called `handle_movie`, not to be confused with our other function `handle_movies`, and annotate it like so:

```py
@app.route("/api/movies/<mid>", methods=["GET", "DELETE"])
def handle_movie(mid: str) -> Response:
    if request.method == "GET":
        # GET logic
    elif request.method == "DELETE":
        # DELETE logic
```

This route is different than the previous one because this one makes use of what is known as a **path parameter**; a parameter passed into the URL path. This value will _always_ be a string so handle it accordingly. Iterate through the list of movies and once you found a movie that has a matching `uuid` as the `mid` path parameter; jsonify and return it back to the client (much like we did in assignment 1):

```py
# ... handle errors.
# ... find movie

return jsonify(movie)
```

Once this is working I want you to move onto the DELETE logic. To get this working, instead of jsonifying and returning the movie dictionary, I want you to instead remove it from `movies`. After you remove it; return a `Response("No content", 204)`.

```py
# ... handle errors.
# ... find and delete movie

return Response("No content", 204)
```

I want you to check for the following error cases:

1. If no movie matches the `mid`; return a `Response("Not found", 404)`.

## Step 4: Testing your code

Delete all of the code in your `test_main.py` file and copy everything in my version on Github into your file. This has more test cases that cover more use cases and error scenarios I outlined earlier in the assignment.

1. Start your server.
2. Using Postman, issue a GET request to http://127.0.0.1:5000/api/movies, you should get a `200 OK` and an empty list in the response.
3. Using Postman, issue a POST request to http://127.0.0.1:5000/api/movies with no request body. You should get a `400 BAD REQUEST`.
4. Using Postman, issue a POST request to http://127.0.0.1:5000/api/movies with the following request body:
   ```json
   {
     "title": null
   }
   ```
   You should get a `400 BAD REQUEST`.
5. Using Postman, issue a POST request to http://127.0.0.1:5000/api/movies with the following request body:
   ```json
   {
     "title": "Interstellar"
   }
   ```
   You should get a `201 CREATED`.
6. Using Postman, issue the same POST same request again. You should get a `409 CONFLICT`.
7. Using Postman, issue a GET request to http://127.0.0.1:5000/api/movies?title=Interstellar, you should get a `200 OK` and the movie back. Copy the `uuid` value.
8. Using Postman and the previously copied `uuid` value, issue a GET request to http://127.0.0.1:5000/api/movies/replace-me-with-copied-uuid, you should get a `200 OK` and the movie back.
9. Using Postman and the previously copied `uuid` value, issue a DELETE request to http://127.0.0.1:5000/api/movies/replace-me-with-copied-uuid, you should get a `204 NO CONTENT` and nothing back.
10. Using Postman, issue a GET request to http://127.0.0.1:5000/api/movies/abcd, you should get a `404 NOT FOUND` back.
11. Using Postman, issue a DELETE request to http://127.0.0.1:5000/api/movies/abcd, you should get a `404 NOT FOUND` back.
12. Kill your server.

## Step 5: Submitting your work

1. Ensure your python environment is activated.
2. Run `pytest`.
3. Once all of your project's test cases are passing, copy the output and submit it on iLearn.

# Assignment 4 - Finishing Touches

Currently we can create new movie entries, get all movie entries, get a movie entry by id, and delete a movie entry. The final thing we want to be able to do is to allow the user to get, add, and delete reviews to/from movie objects.

## Setup

Create two new function called `handle_reviews` and `handle_review`.

```py
@app.route("/api/movies/<mid>/reviews", methods=["GET", "POST"])
def handle_reviews(mid: str) -> Response:
    if request.method == "GET":
        # GET logic
    elif request.method == "POST":
        # POST logic


@app.route("/api/movies/<mid>/reviews/<rid>", methods=["GET", "DELETE"])
def handle_review(mid: str, rid: str) -> Response:
    if request.method == "GET":
        # GET logic
    elif request.method == "DELETE":
        # DELETE logic
```

In the `handle_reviews` function, I want you to be able to list all reviews of a given movie and add a new review. In the `handle_review` function I want you to be able to retrieve a single review and delete a single review from a movie.

## The GET requests

For the `handle_reviews` function, once you get the reviews property from the movie entry, return it back to the client like so:

```py
return jsonify(reviews)
```

Some edge cases I want you to look out for are the following:

1. If no movie matches the `mid`; return a `Response("Not found", status=404)`

For the `handle_review` function, once you get the specific review property from the movie entry, return it back to the client like so:

```py
return jsonify(review)
```

Some edge cases I want you to look out for are the following:

1.  If no movie matches the `mid`; return a `Response("Not found", status=404)`
2.  If no review matches the `rid`; return a `Response("Not found", status=404)`

## The POST request

For the POST request in `handle_reviews`, you need to retrieve the request body like you have done in previous POST request handling. This time you are expecting a request body to be a dictionary that has the following keys: `username` which maps to a string, `score` which maps to a float value between `0.0` and `10.0`, and `review` which maps to a string.

1. First thing you will want to do is retrieve the request body.
2. Validate the request body (request body contains the keys and the values are valid).
3. Construct a new review object:
   ```py
   review = {
       "uuid": uuid.uuid4(),
       "username": request.get_json()["username"],
       "score": request.get_json()["score"],
       "review": request.get_json()["review"]
   }
   ```
4. Append the review to the movie's reviews.
5. Finally return a `Response("Created", status=201)`

Some edge cases I want you to look out for are the following:

1. If no movie matches the `mid`; return a `Response("Not found", status=404)`
2. If the any of the expected keys aren't present in the request body; return a `Response("Bad request", status=400)`
3. If the value of the `username` in the request body isn't a string; return a `Response("Bad request", status=400)`
4. If the value of the `score` in the request body isn't a float between 0 and 10; return a `Response("Bad request", status=400)`
5. If the value of the `review` in the request body isn't a string; return a `Response("Bad request", status=400)`

## The DELETE request

For the DELETE request in `handle_review`, you need to retrieve the specific review entry in a specific movie and then remove it from a movie entry's list of reviews. Once you have successfully removed the review from the movie, return a `Response("No content", status=204)`.

Some edge cases I want you to look out for are the following:

1. If no movie matches the `mid`; return a `Response("Not found", status=404)`
2. If no review matches the `rid`; return a `Response("Not found", status=404)`

## Testing your code

Activating your python environment and running `pytest` will be the best indicator that your code is working as intended. However, if you want to get comfortable with issuing requests follow the steps below:

1. Start your server
2. Using Postman, issue a GET request to http://127.0.0.1:5000/api/movies, you should get a `200 OK` and an empty list in the response.
3. Using Postman, issue a POST request to http://127.0.0.1:5000/api/movies with the following request body:
   ```json
   {
     "title": "Interstellar"
   }
   ```
   You should get a `201 CREATED`.
4. Using Postman, issue a GET request to http://127.0.0.1:5000/api/movies?title=Interstellar, you should get a `200 OK` and the movie back. Copy the `uuid` value.
5. Using Postman and the previously copied `uuid` value, issue a GET request to http://127.0.0.1:5000/api/movies/replace-me-with-copied-uuid, you should get a `200 OK` and the movie back.
6. Using Postman and the previously copied `uuid` value, issue a POST request to http://127.0.0.1:5000/api/movies/replace-me-with-copied-uuid/reviews with the following request body:
   ```json
   {
     "username": "johnsmith",
     "score": 9.5,
     "review": "Great movie!"
   }
   ```
   You should get a 201 CREATED back.
7. Using Postman, issue a GET request to http://127.0.0.1:5000/api/movies?title=Interstellar, you should get a `200 OK` and the movie back with the review back.

## Submitting your code

Run `pytest`; copy the output and submit it in the assignment on iLearn.
