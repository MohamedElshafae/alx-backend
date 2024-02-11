#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config(object):
    """Config class"""
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"
    LANGUAGES = ['en', 'es']


babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def index():
    """index function"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
