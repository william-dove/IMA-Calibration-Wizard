#main.py

import webview
import threading
import json

import sys
import shutil
from pathlib import Path

from app import create_app
from app.api import Api


# Establish static resource directory (bundled with the .exe when compiled using PyInstaller)
if getattr(sys, 'frozen', False):
    # PyInstaller (executable)
    RESOURCE_DIR = Path(sys._MEIPASS)
else:
    # development (running main.py from cmd venv)
    RESOURCE_DIR = Path(__file__).resolve().parent

# Establish persistent user data directory (for report_names.json, reports, etc.) in AppData
DATA_DIR = Path.home()/'AppData'/'Local'/'ImaCalibrationWizard'
REPORTS_DIR = DATA_DIR/'calcart1'/'reports'
REPORT_NAMES_DIR = DATA_DIR/'calcart1'/'report_names.json'

def initialize_user_data():

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    # Copy report names on first launch
    if not REPORT_NAMES_DIR.exists():
        shutil.copy2(
            RESOURCE_DIR/'calcart1'/'report_names.json',
            REPORT_NAMES_DIR
        )

    # Copy default report presets
    for source in (RESOURCE_DIR/'calcart1'/'reports').glob('*.json'):

        destination = REPORTS_DIR/source.name

        if not destination.exists():
            shutil.copy2(source, destination)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == "__main__":

    initialize_user_data()

    # Load report presets (for calcart)
    report_names_dir = DATA_DIR/'calcart1'/'report_names.json'
    with report_names_dir.open('r') as file:
        report_names = json.load(file)

    api = Api()

    app = create_app(api, RESOURCE_DIR, DATA_DIR, report_names)

    threading.Thread(
        target=lambda: app.run(),
        daemon=True
    ).start()

    window = webview.create_window("IMA Calibration Wizard", "http://127.0.0.1:5000", js_api=api)

    api.window = window

    webview.start()