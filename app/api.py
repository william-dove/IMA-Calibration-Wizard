#app/api.py

import webview


class Api:
    def __init__(self):
        '''
        Initializes a window attribute for this class.
        After this class is instantiated, you should add 
        the webview.create_window() object (i.e. the window
        for the app) as an attribute to this class.

        Also initializes attributes to be used within calcart1.html.
        '''
        self.window = None

        self.report_complete = False
        self.calibration_complete = False
        self.save_directory = None

    def get_status(self):
        return {
            "report_complete": self.report_complete,
            "calibration_complete": self.calibration_complete
        }

    def choose_folder(self):
        '''
        Opens a popup to choose a directory where results of the test will
        be saved (excel report, raw data, etc.)
        '''
        result = self.window.create_file_dialog(
            webview.FOLDER_DIALOG
        )

        if not result: # User cancelled
            return None

        directory = result[0]

        self.save_directory = directory

        return directory
    