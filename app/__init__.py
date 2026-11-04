#app/__init__.py

from flask import Flask, render_template, request, redirect, url_for, session
import json
from calcart1.settings import SS_BY_SECTION
from calcart1.report import generate_report

def create_app(api, ROOT_DIR, report_names):
    # Create and configure the app
    app = Flask(__name__)

    # Initialize session variables
    app.secret_key = 'dev'

    @app.before_request
    def initialize_session():
        session.setdefault("report_complete", False)
        session.setdefault('calibration_complete', False)
        session.setdefault('report_dict', {})
        session.setdefault('calibration_dict', {})


    # Define routes

    # Home
    # ~~~~

    @app.route("/")
    def home():
        session.clear() # Clears the session when the user leaves a specific program (e.g. calcart, mycom)
        return render_template("index.html")

    @app.route("/calcart1")
    def calcart1():
        return render_template(
            "calcart1.html",
            report_names=report_names
        )

    @app.route("/mycom")
    def mycom():
        return render_template("mycom.html")

    # User form
    # ~~~~~~~~~

    @app.route("/calcart1/form")
    def calcart1_form():
        return render_template(
            "calcart1_form.html",
            sections=SS_BY_SECTION,
        )

    @app.route("/calcart1/form/load", methods=['POST'])
    def calcart1_load_form():
        name = request.form['report_name']

        with open(f'calcart1/reports/{name}.json', 'r') as file:
            data = json.load(file)

        # Debug
        print(name)
        print(data)

        # Update the session/api
        session['report_dict'] = data
        session['report_complete'] = True
        api.report_complete = True

        return redirect(url_for("calcart1"))

    @app.route("/calcart1/form/submit", methods=['POST'])
    def calcart1_submit_form():
        '''
        Retrieves the user inputs from the HTML, creates a new report preset
        name and filename (if the user inputs a name/filename that already exists, the
        filename is modified to avoid overwriting), saves the report preset, saves
        the report preset name/filename to report_presets.json.
        
        '''
        # Load the user's inputs for the report from the HTML
        data = request.form.to_dict()

        # Determine the name used to save the report
        name = data['report_name']

        if name in report_names:
            i = 1
            while f'{name} ({i})' in report_names:
                i += 1
            name = f'{name} ({i})'

        data['report_name'] = name

        # Add the filename to report_names.json, save the report.
        report_names.append(name)
        report_names_dir = ROOT_DIR/'calcart1'/'report_names.json'
        with report_names_dir.open('w') as file: 
            json.dump(report_names, file, indent=4)

        filename = f'{name}.json'
        report_file_dir = ROOT_DIR/'calcart1'/'reports'/filename
        with report_file_dir.open('w') as file:
            json.dump(data, file, indent=4)

        # Debug
        print(name)
        print(data)

        # Update the session
        session['report_dict'] = data
        session['report_complete'] = True
        api.report_complete = True

        return redirect(url_for("calcart1"))

    # Calibration test
    # ~~~~~~~~~~~~~~~~

    @app.route("/calcart1/test")
    def calcart1_test():
        return render_template('calcart1_test.html')

    @app.route("/calcart1/test/submit", methods=['POST'])
    def calcart1_submit_test():
        data = request.form.to_dict()

        # Debug
        print('Calibration Test Data: ')
        print(data)

        # Update the session
        session['calibration_dict'] = data
        session['calibration_complete'] = True
        api.calibration_complete = True
        
        return redirect(url_for("calcart1"))

    # Generating the report
    # ~~~~~~~~~~~~~~~~~~~~~

    @app.route("/calcart1/generate-report")
    def calcart1_generate_report():

        generate_report(
            api.save_directory,
            ROOT_DIR,
            session['report_dict'],
            session['calibration_dict']
        )
        
        return "Making report :)"


    return app

