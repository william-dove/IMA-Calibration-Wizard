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



## To Do

- Currently the report saving/loading mechanism does not work. To get this to behave with PyInstaller, I will need to update the code such that
`report_names.json` and the existing/saved report `.json` files themselves are stored properly in the user's AppData folder, using pathlib.