#app/__init__.py

from flask import Flask, render_template, request
from report.settings import SS_BY_SECTION

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
        return render_template(
            "calcart1_form.html",
            sections=SS_BY_SECTION
        )

    @app.route("/calcart1/form/submit", methods=['POST'])
    def calcart1_submit_form():
        data = request.form.to_dict()
        print(data)
        return "Success"

    @app.route("/mycom")
    def mycom():
        return render_template("mycom.html")


    return app

