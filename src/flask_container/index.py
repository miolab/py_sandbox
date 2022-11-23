from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response

app = Flask(__name__)


def main():
    app.debug = True
    app.run(
        host='127.0.0.1',
        port='5000'
    )


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    main()
