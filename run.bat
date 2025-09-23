@echo off
echo ========================================
echo Instagram Influencer Analysis Tool
echo ========================================
echo.

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo ❌ Virtual environment not found!
    echo Please run install.bat first
    pause
    exit /b 1
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Run main script
echo 🚀 Running tool...
python main.py

echo.
echo 👋 Goodbye!
pause

