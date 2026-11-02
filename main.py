#main.py
from flask import Flask
import webview
import threading

from app import create_app


app = create_app()

def run_app():
    app.run()


if __name__ == "__main__":
    threading.Thread(
        target=run_app,
        daemon=True
    ).start()

    webview.create_window("IMA Calibration Wizard", "http://127.0.0.1:5000")

    webview.start()