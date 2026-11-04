#main.py

import webview
import threading
import json

import sys
import shutil
from pathlib import Path

from app import create_app
from app.api import Api


# Establish root directory
if getattr(sys, 'frozen', False):
    # PyInstaller (executable)
    ROOT_DIR = Path(sys._MEIPASS)
else:
    # development (running main.py from cmd venv)
    ROOT_DIR = Path(__file__).resolve().parent


if __name__ == "__main__":

    # Load report presets (for calcart)
    report_names_dir = ROOT_DIR/'calcart1'/'report_names.json'
    with report_names_dir.open('r') as file:
        report_names = json.load(file)

    api = Api()

    app = create_app(api, ROOT_DIR, report_names)

    threading.Thread(
        target=lambda: app.run(),
        daemon=True
    ).start()

    window = webview.create_window("IMA Calibration Wizard", "http://127.0.0.1:5000", js_api=api)

    api.window = window

    webview.start()