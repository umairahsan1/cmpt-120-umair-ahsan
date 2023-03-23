# import the flask package for making rest apis.
from flask import *

# create an instance of a Flask object.
app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    '''
    This is our base route. When visited, we get the text "Hello, world!"
    '''
    return "Hello, world!"


# run our application
if __name__ == '__main__':
    app.run()
