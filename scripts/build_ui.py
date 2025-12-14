import subprocess
import sys

def run(cmd):
    print(f"Выполняется: {cmd}")
    result = subprocess.run(cmd, shell=True)
    if result.returncode != 0:
        print(f"Ошибка при выполнении: {cmd}")
        sys.exit(result.returncode)

if __name__ == "__main__":
    run("pyside6-rcc icons/resources.qrc -o app/ui/resources_rc.py")
    run("pyside6-uic templates/main.ui -o app/ui/main_window.py")
    print("Готово!")
