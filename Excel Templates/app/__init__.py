#app/__init__.py

import os
from flask import Flask, render_template

def create_app(test_config=None):
    # Create and configure the app
    app = Flask(__name__)

    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route("/")
    def home():
        return render_template("index.html")

    return app

