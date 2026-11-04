# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

datas = [('C:/Users/dovew/OneDrive - IMA Group/Documenti/IMA Calibration Wizard/app/templates/base.html', 'app/templates'), ('C:/Users/dovew/OneDrive - IMA Group/Documenti/IMA Calibration Wizard/app/templates/calcart1.html', 'app/templates'), ('C:/Users/dovew/OneDrive - IMA Group/Documenti/IMA Calibration Wizard/app/templates/calcart1_form.html', 'app/templates'), ('C:/Users/dovew/OneDrive - IMA Group/Documenti/IMA Calibration Wizard/app/templates/calcart1_test.html', 'app/templates'), ('C:/Users/dovew/OneDrive - IMA Group/Documenti/IMA Calibration Wizard/app/templates/index.html', 'app/templates'), ('C:/Users/dovew/OneDrive - IMA Group/Documenti/IMA Calibration Wizard/app/templates/mycom.html', 'app/templates'), ('C:/Users/dovew/OneDrive - IMA Group/Documenti/IMA Calibration Wizard/app/static/css/style.css', 'app/static/css'), ('C:/Users/dovew/OneDrive - IMA Group/Documenti/IMA Calibration Wizard/app/static/images/IMA.png', 'app/static/images'), ('C:/Users/dovew/OneDrive - IMA Group/Documenti/IMA Calibration Wizard/app/static/js/script.js', 'app/static/js'), ('C:/Users/dovew/OneDrive - IMA Group/Documenti/IMA Calibration Wizard/calcart1/report_names.json', 'calcart1'), ('C:/Users/dovew/OneDrive - IMA Group/Documenti/IMA Calibration Wizard/calcart1/template.xltx', 'calcart1'), ('C:/Users/dovew/OneDrive - IMA Group/Documenti/IMA Calibration Wizard/calcart1/reports/Sample Report 1.json', 'calcart1/reports'), ('C:/Users/dovew/OneDrive - IMA Group/Documenti/IMA Calibration Wizard/calcart1/reports/www (1).json', 'calcart1/reports'), ('C:/Users/dovew/OneDrive - IMA Group/Documenti/IMA Calibration Wizard/calcart1/reports/www.json', 'calcart1/reports'), ('C:/Users/dovew/OneDrive - IMA Group/Documenti/IMA Calibration Wizard/calcart1/reports/Sample Report 1/Sample Report 1.xlsx', 'calcart1/reports/Sample Report 1')]
binaries = []
hiddenimports = []
tmp_ret = collect_all('webview')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]
tmp_ret = collect_all('xlwings')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]


a = Analysis(
    ['C:/Users/dovew/OneDrive - IMA Group/Documenti/IMA Calibration Wizard/main.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='IMA_Calibration_Wizard',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:/Users/dovew/OneDrive - IMA Group/Documenti/IMA Calibration Wizard/icon.ico'],
)
