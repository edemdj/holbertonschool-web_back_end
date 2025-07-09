#!/usr/bin/env python3
""" use Flask with Babel """


from flask import Flask, render_template, request
from flask_babel import Babel, g
import pytz
from pytz.exceptions import UnknownTimeZoneError


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """ config class """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    """ get the locale from the request """
    # Paramètre d'URL
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # Langue de l'utilisateur connecté
    user = getattr(g, 'user', None)
    if user:
        user_locale = user.get('locale')
        if user_locale in app.config['LANGUAGES']:
            return user_locale

    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_timezone():
    """ get the timezone from the user """
    return app.config.get('BABEL_DEFAULT_TIMEZONE', 'UTC')


def get_user():
    """ get the user from the request """
    try:
        user = int(request.args.get("login_as"))
        return users.get(user)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """ set user """
    g.user = get_user()


@app.route('/')
def index():
    """ route for index"""
    return render_template('6-index.html')


babel = Babel()
babel.init_app(app, locale_selector=get_locale, timezone_selector=get_timezone)
