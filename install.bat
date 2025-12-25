@echo off
REM Checking for the presence of a virtual environment
IF NOT EXIST .venv (
    echo Virtual environment not found. Creating...
    python -m venv .venv
)

REM Activate the virtual environment
call .venv\Scripts\activate

REM Checking whether dependencies are installed
IF EXIST requirements.txt (
    echo install dependencies...
    pip install --upgrade pip
    pip install -r requirements.txt
)

pause

REM Activate the virtual environment
call .venv\Scripts\activate

REM Launch the application without the console
start "" .venv\Scripts\pythonw.exe -m app.main