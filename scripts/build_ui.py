import subprocess
import sys
import pathlib

def run(cmd):
    print(f"In progress: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"Error: {cmd}")
        sys.exit(result.returncode)

def replace_imports():
    files = [
        "app/ui/main_window.py",
        "app/ui/debug_param_widget.py"
    ]

    for file in files:
        ui_file = pathlib.Path(file)
        text = ui_file.read_text(encoding="utf-8")
        text = text.replace("import resources_rc", "from app.ui import resources_rc")
        ui_file.write_text(text, encoding="utf-8")

def convertor():
    run("pyside6-rcc icons/resources.qrc -o app/ui/resources_rc.py")
    run("pyside6-uic templates/main.ui -o app/ui/main_window.py")
    run("pyside6-uic templates/debug.ui -o app/ui/debug.py")
    run("pyside6-uic templates/assignment.ui -o app/ui/assignment.py")
    run("pyside6-uic templates/toys.ui -o app/ui/toys.py")
    run("pyside6-uic templates/settings.ui -o app/ui/settings.py")
    run("pyside6-uic templates/debug_param_widget.ui -o app/ui/debug_param_widget.py")


if __name__ == "__main__":
    convertor()
    replace_imports()
    print("Complete!")
