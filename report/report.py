#report.py

# Probably doesn't work currently!!

import xlwings as xw
from settings import SETTINGS


def fill():
    with xw.App(visible=False) as xwa:
        wb = xwa.books.open('template.xltx')
        ws = wb.sheets['Sheet1']

        # Fill in header info
        for s in SETTINGS:
            if s.report_cell is not None:
                val = self.config.get(s.section, s.key, cast=str)
                cell = s.report_cell
                ws[cell].value = val

        # Fill in setpoint results (currently for 1 UUT only.)
        report_row = 60 # The "setpoint" column in the report is in cells A60:A70,
                        # The "standard" column is B60:B70, and the "instrument"
                        # column is C60:C70.
        for sp_num, row in results.iterrows():
            sp_cell = f'A{report_row}'
            std_cell = f'B{report_row}'
            inst_cell = f'C{report_row}'

            ws[sp_cell].value = sp_num
            ws[std_cell].value = row['reference/standard pressure']
            ws[inst_cell].value = row['uut 1']

            report_row += 1

        save_path = os.path.join(self.resultsdir, 'report.xlsx')
        wb.save(save_path)

        try:
            fill()
        except Exception as e:
            self.log(f'[ERROR] {e}.\nFailed to open Excel file. Check if the file is already open in Excel.')
def generate_report():
    '''
    Generates an Excel report using template.xltx
    '''
