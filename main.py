#main.py
from flask import Flask
import webview
import threading
import configparser
import os
import json

from app import create_app


# Load report presets (for calcart)
with open('calcart1/report_names.json', 'r') as file:
    report_names = json.load(file)

# To write back to json:
# with open('calcart1/report_presets.json', 'w') as file:
#   json.dump(report_presets, file, indent=4)


app = create_app(report_names)

def run_app():
    app.run()


if __name__ == "__main__":
    threading.Thread(
        target=run_app,
        daemon=True
    ).start()

    webview.create_window("IMA Calibration Wizard", "http://127.0.0.1:5000")

    webview.start()