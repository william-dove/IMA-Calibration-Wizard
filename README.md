# IMA Calibration Wizard

## Installation

Installation was carried out using a conda-based python environment.

1. Create a virtual environment and install dependancies.

    `conda activate`

    `python -m venv .venv`

    `.venv\Scripts\activate`

    `python -m pip install --upgrade pip`

    `pip install -r requirements.txt`


2. Compile using PyInstaller. (Second argument is optional app name; do not include `.exe`. New distributions default to the app name above.)

    `python build.py IMA_Calibration_Wizard`
