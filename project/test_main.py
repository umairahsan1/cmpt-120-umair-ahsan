import json
from main import app


def test_hello_world():
    response = app.test_client().get("/")
    assert response.status_code == 200


def test_list_movies():
    response = app.test_client().get("/api/movies")
    movies = json.loads(response.data.decode("utf-8"))
    assert len(movies) == 4


def test_list_movies_with_query_param():
    response = app.test_client().get("/api/movies?title=Frozen")
    movies = json.loads(response.data.decode("utf-8"))
    assert len(movies) == 1


def test_list_movies_with_query_params():
    response = app.test_client().get("/api/movies?title=Frozen&title=Moana")
    movies = json.loads(response.data.decode("utf-8"))
    assert len(movies) == 2
