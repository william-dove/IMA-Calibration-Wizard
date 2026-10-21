#iniconfig.py

import configparser
from io import StringIO
import os

class ConfigLoader:
    def __init__(self):
        self.config = configparser.ConfigParser(interpolation=None)

        