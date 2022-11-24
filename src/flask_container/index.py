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
def hello_world_top():
    return 'Top'


@app.route('/hello')
def hello_world_detail():
    return 'Hello, World!'


@app.route('/hello/<user_name>')
def hello_user_name(user_name):
    return f'Hello, {user_name}!'


if __name__ == '__main__':
    main()
