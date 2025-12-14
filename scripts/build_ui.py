import subprocess
import sys
import pathlib

def run(cmd):
    print(f"Выполняется: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"Ошибка при выполнении: {cmd}")
        sys.exit(result.returncode)

def replace_imports():
    ui_file = pathlib.Path("app/ui/main_window.py")
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

if __name__ == "__main__":
    convertor()
    replace_imports()
    print("Готово!")
