# IMA Calibration Wizard

## Overview

This app uses Flask and Pywebview to run a local Python web application.

Users may input information in the "Cal Cart" mode, and an Excel report is generated based on inputs using the `xlwings` Python library.

The different fields to be included on the report, their default values, and which cell to write the data to on the Excel report, are stored in `settings.py`. To update the default values, just add a new default in the Python dataclass. To add new fields to the report, add them to the dataclass, specify a valid cell in the Excel report template, and ensure the template is set up for the value to go in that cell.

## Version Requirements

- Anaconda version 0.7.0
- Python 3.19.9

## Installation

Installation was carried out using a conda-based python environment. To install, execute the commands below on a machine with conda installed.

1. Create a virtual environment and install dependancies.

    `conda activate`

    `python -m venv .venv`

    `.venv\Scripts\activate`

    `python -m pip install --upgrade pip`

    `pip install -r requirements.txt`


2. Compile using PyInstaller. (Second argument is optional app name; do not include `.exe`. New distributions default to the app name above.)

    `python build.py IMA_Calibration_Wizard`

From here, a shortcut to the application can be made if desired.

## Future

This framework can be easily adapted/extended to generate reports for other devices, such as the Mycom test rig.

## To Do

- Create a more detailed instruction/readme