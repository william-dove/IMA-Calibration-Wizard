# IMA Calibration Wizard

## Installation

1. Create a virtual environment and install dependancies.

    `python -m venv .venv`

    `.venv\Scripts\activate`

    `python -m pip install --upgrade pip`

    `pip install -r requirements.txt`


2. Compile using PyInstaller. (Second argument is optional app name; do not include `.exe`. New distributions default to the app name above.)

    `python build.py IMA_Calibration_Wizard`
