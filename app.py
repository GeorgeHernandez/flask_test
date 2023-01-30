"""Flask is a micro web framework"""
from flask import Flask

app = Flask(__name__)

# tell the router which URL will trigger the function
@app.route("/")
def index():
    """The following is returned by the URL above."""
    # return f'Hello World!'
    return "Hello <b>World!!</b>"


if __name__ == "__main__":
    app.run()
