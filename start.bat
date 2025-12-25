@echo off
REM Activate the virtual environment
call .venv\Scripts\activate

REM Launch the application without the console
start "" .venv\Scripts\pythonw.exe -m app.main