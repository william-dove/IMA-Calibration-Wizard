#calcart1/report.py
import xlwings as xw
import os
from calcart1.settings import SETTINGS


def generate_report(save_dir, ROOT_DIR, report_dict, calibration_dict):
    '''
    Creates an Excel report using xlwings. The directory where the Excel report is saved will be 
    `calcart1/reports/name/`, where name is the name of the report as given in 
    report_names.json.

    :param report_dict: the `session['report']` dict from Flask app
    :param calibration_dict: the `session['calibration'] dict from Flask app
    '''

    # Make a save directory/filename based on the user-chosen directory
    name = report_dict['report_name']
    os.makedirs(save_dir, exist_ok=True)
    save_path = os.path.join(save_dir, f'{name}.xlsx')

    # Define the template path via the constant system path RESOURCE_DIR.
    template_dir = ROOT_DIR/'calcart1'/'template.xltx'

    with xw.App(visible=False) as xwa:
        wb = xwa.books.open(str(template_dir))
        ws = wb.sheets['Sheet1']

        # Fill in header info
        # ~~~~~~~~~~~~~~~~~~~

        for s in SETTINGS:
            if s.report_cell is not None:
                val = report_dict[s.key] or ''
                cell = s.report_cell
                ws[cell].value = val


        # Fill in setpoint results (currently for 1 DUT only.)
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # Figure out how many setpoints there are (3 dictionary entries per
        #   setpoint, plus one entry for the reference offset.)
        num_setpoints = (len(calibration_dict) - 1) // 3

        # Choose the row on the excel sheet to start filling in setpoint data
        report_row = 60 # The "setpoint" column in the report is in cells A60:A70,
                        # The "standard" column is B60:B70, and the "instrument"
                        # column is C60:C70.

        # Fill in each row
        for i in range(num_setpoints):
            sp_cell = f'A{report_row + i}'
            ref_cell = f'B{report_row + i}'
            dut_cell = f'C{report_row + i}'

            ws[sp_cell].value = calibration_dict[f'setpoint[{i+1}]']
            ws[ref_cell].value = calibration_dict[f'standard[{i+1}]']
            ws[dut_cell].value = calibration_dict[f'instrument[{i+1}]']


        # Save results 
        # ~~~~~~~~~~~~

        wb.save(save_path)

