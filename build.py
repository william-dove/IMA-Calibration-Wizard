#build.py

'''
This script creates a new executable distribition in the /dist folder. All dependancies are 
included in the single .exe file.

IMPORTANT: Execute this script from the virtual environment to ensure the correct python
dependancies are installed.

Assumes PyInstaller has been installed to the virtual environment (which it has).
'''

import subprocess
import sys
from pathlib import Path


# Configuration

ROOT_DIR = Path(__file__).resolve().parent

APP_NAME = sys.argv[1] if len(sys.argv) > 1 else "IMA_Calibration_Wizard"

MAIN_FILE = ROOT_DIR / "main.py"

# Directories containing application resources
RESOURCE_DIRS = [
    ROOT_DIR / "app",
    ROOT_DIR / "calcart1",
]

# Optional application icon
ICON_PATH = ROOT_DIR / "icon.ico"


# Check for proper interpreter and virtual environment before building
if "conda" not in sys.base_prefix.lower():
    print("ERROR: Expected a Conda-based Python environment.")
    sys.exit(1)

if sys.prefix == sys.base_prefix:
    print("ERROR: Activate the project venv first.")
    sys.exit(1)


def build():

    command = [
        sys.executable,
        "-m", "PyInstaller",

        "--noconfirm",
        "--clean",

        "--onefile",
        "--windowed",

        "--name", APP_NAME,

        "--distpath", str(ROOT_DIR / "dist"),
        "--workpath", str(ROOT_DIR / "build"),

        "--icon", str(ICON_PATH),
    ]

    # Include all non-Python resource files while preserving their original directory structure.
    for directory in RESOURCE_DIRS:

        if not directory.exists():
            continue

        for file in directory.rglob("*"):

            if not file.is_file():
                continue

            # Skip Python source and cache files
            if file.suffix in {".py", ".pyc", ".pyo"}:
                continue

            if "__pycache__" in file.parts:
                continue

            # Destination relative to the bundle root
            destination = file.relative_to(ROOT_DIR).parent

            command.extend([
                "--add-data",
                f"{file};{destination}"
            ])

    # Collect additional resources and imports for dependencies that may use dynamic imports.
    command.extend([
        "--collect-all", "webview",
        "--collect-all", "xlwings",
    ])

    # Main entry point
    command.append(str(MAIN_FILE))

    # Execute PyInstaller from the project directory
    print("\nStarting PyInstaller build...\n")

    subprocess.run(
        command,
        cwd=ROOT_DIR,
        check=True
    )

    print("\n" + "=" * 50)
    print("Build Completed Successfully")
    print("=" * 50)

    print(
        f"\nExecutable:\n"
        f"{ROOT_DIR / 'dist' / (APP_NAME + '.exe')}"
    )


if __name__ == "__main__":
    build()
