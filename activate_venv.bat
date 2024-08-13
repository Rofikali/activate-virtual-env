@echo off
REM Run the Python script to list directory contents
python check_venv.py

REM Check if venv folder exists and activate it
if exist venv (
    echo Found venv. Activating...
    call venv\Scripts\activate
) else (
    echo venv not found in the current directory.
)
