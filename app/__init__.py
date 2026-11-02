#app/__init__.py

from flask import Flask, render_template, Response, request, redirect, url_for, session
import json
from report.settings import SS_BY_SECTION

def create_app():
    # Create and configure the app
    app = Flask(__name__)

    # Initialize session variables
    app.secret_key = 'dev'

    @app.before_request
    def initialize_session():
        session.setdefault("report_complete", False)
        session.setdefault('calibration_complete', False)


    # Define routes

    @app.route("/")
    def home():
        session.clear() # Clears the session when the user leaves a specific program (e.g. calcart, mycom)
        return render_template("index.html")

    @app.route("/calcart1")
    def calcart1():
        return render_template(
            "calcart1.html",
        )

    @app.route("/calcart1/form")
    def calcart1_form():
        return render_template(
            "calcart1_form.html",
            sections=SS_BY_SECTION,
        )

    @app.route("/calcart1/form/load", methods=['POST'])
    def calcart1_load_form():
        file = request.files["report_file"]
        print(file.filename)

        session['report_complete'] = True

        return redirect(url_for("calcart1"))

    @app.route("/calcart1/form/submit", methods=['POST'])
    def calcart1_submit_form():
        data = request.form.to_dict()
        json_data = json.dumps(data, indent=4)

        session['report_complete'] = True

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
        return render_template('calcart1_test.html')

    @app.route("/calcart1/test/submit", methods=['POST'])
    def calcart1_submit_test():
        data = request.form.to_dict()
        print(data)

        session['calibration_complete'] = True
        
        return redirect(url_for("calcart1"))

    @app.route("/mycom")
    def mycom():
        return render_template("mycom.html")


    return app

