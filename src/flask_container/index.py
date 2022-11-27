"""Flask Sample about rendering template.
"""
from flask import Flask
from flask import render_template

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
@app.route('/hello/<user_name>')
def hello_user_name(user_name=None):
    return render_template(
        'index.html',
        user_name=user_name
    )


if __name__ == '__main__':
    main()
