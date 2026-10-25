@echo off
title Plant Disease Recognition System - One-Click Launcher
cd /d "%~dp0"

echo ================================================================
echo    Plant Disease Recognition System - 1-Click Setup ^& Launcher
echo ================================================================
echo.

:: 1. Check Python installation
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Python is not installed or not found on PATH.
    echo Please download and install Python from https://www.python.org/
    pause
    exit /b 1
)

:: 2. Check and Install Python Dependencies
echo [1/3] Checking and installing dependencies...
python -m pip install -r requirements.txt
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Dependency installation encountered an issue.
    pause
    exit /b 1
)

:: 3. Check and Download Model Weights
echo.
echo [2/3] Checking pre-trained model weights...
python download_model.py
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Failed to obtain pre-trained model weights.
    pause
    exit /b 1
)

:: 4. Launch Streamlit Dashboard
echo.
echo [3/3] Launching Plant Disease Recognition Dashboard...
echo URL: http://localhost:8501
echo (Press Ctrl+C to stop the application)
echo.
python -m streamlit run main.py

pause
