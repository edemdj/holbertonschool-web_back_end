#!/usr/bin/env python3
""" initiation of a Flask app with Babel for i18n """


from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@app.route('/')
def index():
    """ route for index"""
    return render_template('0-index.html')
