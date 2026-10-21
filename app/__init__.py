#app/__init__.py

import os
from flask import Flask, render_template

def create_app():
    # Create and configure the app
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/calcart1")
    def calcart1():
        return render_template("calcart1.html")

    @app.route("/calcart1/form")
    def calcart1_form():
        return render_template("calcart1_form.html")

    @app.route("calcart1/form/submit")
    def calcart1_submit_form():
        return

    @app.route("/mycom")
    def mycom():
        return render_template("mycom.html")


    return app

