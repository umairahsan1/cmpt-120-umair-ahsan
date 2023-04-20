import uuid
from flask import *

# create an instance of a Flask object.
app = Flask(__name__)

# our document storage.
movies = []


@app.route("/", methods=["GET"])
def hello_world() -> Response:
    return Response("Hello world!", status=200)


@app.route("/api/movies", methods=["GET", "POST"])
def handle_movies() -> Response:
    pass


@app.route("/api/movies/<mid>", methods=["GET", "DELETE"])
def handle_movie(mid: str) -> Response:
    pass


@app.route("/api/movies/<mid>/reviews", methods=["GET", "POST"])
def handle_reviews(mid: str) -> Response:
    pass


@app.route("/api/movies/<mid>/reviews/<rid>", methods=["GET", "DELETE"])
def handle_review(mid: str, rid: str) -> Response:
    pass


# run our application
if __name__ == '__main__':
    app.run()
