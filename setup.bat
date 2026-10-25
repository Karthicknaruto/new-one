@echo off
title Plant Disease Recognition System - Setup
cd /d "%~dp0"

echo ========================================================
echo       Plant Disease Recognition System - Setup
echo ========================================================
echo.

:: 1. Check Python
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python is not installed or not in PATH.
    pause
    exit /b 1
)

:: 2. Install requirements
echo [1/2] Installing required Python packages...
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

:: 3. Download model
echo.
echo [2/2] Verifying pre-trained model...
python download_model.py

echo.
echo ========================================================
echo  Setup Completed Successfully!
echo  Run "run.bat" to start the Streamlit web application.
echo ========================================================
pause
