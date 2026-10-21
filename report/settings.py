from dataclasses import dataclass
from collections import defaultdict

@dataclass(frozen=True)
class S:
    section: str
    key: str
    label: str
    default: str = ''
    input_type: str = 'text'
    report_cell: str = None


SETTINGS = [
    # --------------------
    # Project Information
    # --------------------
    S(
        section="project_info",
        key="company",
        label="Company",
        report_cell='B3',
    ),
    S(
        section="project_info",
        key="project",
        label="Project",
        report_cell='B4',
    ),
    S(
        section="project_info",
        key="service_number",
        label="Service Number",
        report_cell='B5',
    ),
    S(
        section="project_info",
        key="machine",
        label="Machine",
        report_cell='B6',
    ),
    S(
        section="project_info",
        key="location",
        label="Location",
        report_cell='B7',
    ),
    S(
        section="project_info",
        key="date",
        label="Date",
        input_type='date',
        report_cell='F2',
    ),
    S(
        section="project_info",
        key="calibration_type",
        label="Calibration Type",
        report_cell = 'F5',
    ),
    S(
        section="project_info",
        key="procedure",
        label="Procedure",
        report_cell='F6',
    ),
    S(
        section="project_info",
        key="calibration",
        label="Calibration",
        report_cell='F7',
    ),
    # --------------------
    # Device Under Test (DUT) Information
    # --------------------
    S(
        section="dut_info",
        key="dut_manufacturer",
        label="Manufacturer",
        report_cell='C10',
    ),
    S(
        section="dut_info",
        key="dut_model_number",
        label="Model Number",
        report_cell='C11',
    ),
    S(
        section="dut_info",
        key="dut_serial_number",
        label="Serial Number",
        report_cell='C12',
    ),
    S(
        section="dut_info",
        key="dut_tag_id_number",
        label="Tag ID Number",
        report_cell='C13',
    ),
    S(
        section="dut_info",
        key="dut_range",
        label="Range",
        report_cell='C14',
    ),
    S(
        section="dut_info",
        key="dut_accuracy",
        label="Device Accuracy",
        report_cell='C15',
    ),
    S(
        section="dut_info",
        key="dut_output_signal",
        label="Output Signal",
        report_cell='C16',
    ),
    # --------------------
    # Reference Device Information
    # --------------------
    S(
        section='ref_info',
        key='ref_manufacturer',
        label='Manufacturer',
        report_cell='G10',
    ),
    S(
        section='ref_info',
        key='ref_model_number',
        label='Model Number',
        report_cell='G11',
    ),
    S(
        section='ref_info',
        key='ref_serial_number',
        label='Serial Number',
        report_cell='G12',
    ),
    S(
        section="ref_info",
        key="ref_calibration_date",
        label="Calibration Date",
        input_type='date',
        report_cell='G13',
    ),
    S(
        section="ref_info",
        key="ref_calibration_due_date",
        label="Calibration Due Date",
        input_type='date',
        report_cell='G14',
    ),
    S(
        section="ref_info",
        key="ref_accuracy",
        label="Standard Accuracy",
        report_cell='G15',
    ),
    S(
        section="ref_info",
        key="ref_accuracy_ratio",
        label="Accuracy Ratio",
        report_cell='G16',
    ),
]

SS_BY_SECTION = defaultdict(dict)
for s in SETTINGS:
    SS_BY_SECTION[s.section][s.key] = s
SS_BY_SECTION = dict(SS_BY_SECTION)