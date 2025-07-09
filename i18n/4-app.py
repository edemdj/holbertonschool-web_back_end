#!/usr/bin/env python3
""" use Flask with Babel """


from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """ config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    """ get the locale from the request """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone():
    """ get the timezone from the user """
    return app.config.get('BABEL_DEFAULT_TIMEZONE', 'UTC')


@app.route('/')
def index():
    """ route for index"""
    return render_template('4-index.html')


babel = Babel()
babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)
