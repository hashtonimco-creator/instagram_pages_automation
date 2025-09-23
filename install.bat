@echo off
echo ========================================
echo Instagram Influencer Analysis Tool
echo ========================================
echo.

REM Check Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed!
    echo Please download and install Python 3.7+ from https://python.org
    pause
    exit /b 1
)

echo ✅ Python is installed
echo.

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo ❌ Error creating virtual environment
    pause
    exit /b 1
)

echo ✅ Virtual environment created
echo.

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo ❌ Error activating virtual environment
    pause
    exit /b 1
)

echo ✅ Virtual environment activated
echo.

REM Upgrade pip
echo 📦 Upgrading pip...
python -m pip install --upgrade pip
echo.

REM Install requirements
echo 📦 Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Error installing dependencies
    pause
    exit /b 1
)

echo ✅ Dependencies installed
echo.

REM Run setup script
echo 🚀 Running setup script...
python scripts\setup.py
if errorlevel 1 (
    echo ❌ Setup error
    pause
    exit /b 1
)

echo.
echo ========================================
echo ✅ Installation and setup completed successfully!
echo ========================================
echo.
echo 📋 Next steps:
echo 1. Prepare your Sanjab account
echo 2. Run the tool with the following command:
echo    python main.py
echo.
echo 📖 For more guidance, read README.md
echo.
pause

