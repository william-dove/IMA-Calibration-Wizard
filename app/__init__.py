#app/__init__.py

from flask import Flask, render_template, Response, request, redirect, url_for, session
import json
from report.settings import SS_BY_SECTION

def create_app():
    # Create and configure the app
    app = Flask(__name__)
    app.secret_key = 'dev'

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/calcart1")
    def calcart1():
        return render_template(
            "calcart1.html",
            report_complete=False,
            calibration_complete=False
        )

    @app.route("/calcart1/form")
    def calcart1_form():
        return render_template(
            "calcart1_form.html",
            sections=SS_BY_SECTION,
            saved=session.get("saved", False)
        )

    @app.route("/calcart1/form/load", methods=['POST'])
    def calcart1_load_form():
        file = request.files["report_file"]
        print(file.filename)
        return redirect(url_for("calcart1"))

    @app.route("/calcart1/form/submit", methods=['POST'])
    def calcart1_submit_form():
        data = request.form.to_dict()
        json_data = json.dumps(data, indent=4)

        session['saved'] = True

        return Response(
            json_data,
            mimetype="application/json",
            headers={
                "Content-Disposition":
                "attachment; filename=report_information.json"
            }
        )

    @app.route("/calcart1/test")
    def calcart1_test():
        return "Test beginning"

    @app.route("/mycom")
    def mycom():
        return render_template("mycom.html")


    return app

