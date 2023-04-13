import json
import pytest
from main import *

OK = "200 OK"
CREATED = "201 CREATED"
NO_CONTENT = "204 NO CONTENT"
BAD_REQUEST = "400 BAD REQUEST"
NOT_FOUND = "404 NOT FOUND"
CONFLICT = "409 CONFLICT"


test_data = [
    {
        "title": "Moana",
        "uuid": "ac5cc608-4d5a-47c5-ab72-06d29bc2a381",
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
        "uuid": "ac5cc608-4d5a-47c5-ab72-06d29bc2a383",
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
        "uuid": "ac5cc608-4d5a-47c5-ab72-06d29bc2a385",
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
        "uuid": "ac5cc608-4d5a-47c5-ab72-06d29bc2a387",
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


@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture(autouse=True)
def setup_and_teardown():
    global movies
    for movie in test_data:
        movies.append(movie)
    yield  # run test
    movies = []


class TestClass:

    def test_list_movies(self, client):
        response = client.get("/api/movies")
        assert response.status == OK
        movies = json.loads(response.data.decode("utf-8"))
        assert len(movies) == 4

    def test_list_movies_with_query_parameter(self, client):
        response = client.get("/api/movies?title=Frozen")
        assert response.status == OK
        movies = json.loads(response.data.decode("utf-8"))
        assert len(movies) == 1

    def test_list_movies_with_query_parameters(self, client):
        response = client.get("/api/movies?title=Frozen&title=Moana")
        assert response.status == OK
        movies = json.loads(response.data.decode("utf-8"))
        assert len(movies) == 2

    def test_add_movie(self, client):
        response = client.post("/api/movies", json={"title": "The Lion King"})
        assert response.status == CREATED
        response = client.get("/api/movies?title=The%20Lion%20King")
        movies = json.loads(response.data.decode("utf-8"))
        assert len(movies) == 1

    def test_add_movie_null_request_body(self, client):
        response = client.post("/api/movies")
        assert response.status == BAD_REQUEST

    def test_add_movie_null_title(self, client):
        response = client.post("/api/movies", json={"title": None})
        assert response.status == BAD_REQUEST

    def test_add_duplicate_movie(self, client):
        response = client.post("/api/movies", json={"title": "Interstellar"})
        assert response.status == CREATED
        response = client.post("/api/movies", json={"title": "Interstellar"})
        assert response.status == CONFLICT

    def test_get_movie(self, client):
        response = client.get(
            f"/api/movies/ac5cc608-4d5a-47c5-ab72-06d29bc2a381")
        assert response.status == OK
        movie = json.loads(response.data.decode("utf-8"))
        assert movie["title"] == "Moana"

    def test_delete_movie(self, client):
        response = client.delete(
            "/api/movies/ac5cc608-4d5a-47c5-ab72-06d29bc2a387")
        assert response.status == NO_CONTENT

    def test_get_not_found(self, client):
        response = client.get("/api/movies/abcd")
        assert response.status == NOT_FOUND

    def test_delete_not_found(self, client):
        response = client.delete("/api/movies/abcd")
        assert response.status == NOT_FOUND
