@echo off

python -c "import bcrypt" >nul 2>&1

IF %ERRORLEVEL% NEQ 0 (
    echo Bcrypt is not installed. Installing...
    pip install bcrypt
) 


echo Running script..

python main.py
pause