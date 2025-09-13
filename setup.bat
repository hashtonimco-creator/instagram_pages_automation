@echo off
echo 🚀 راه‌اندازی پروژه Sanjab Instagram Analytics Scraper
echo ============================================================

echo.
echo 1. بررسی Python...
python --version
if %errorlevel% neq 0 (
    echo ❌ Python نصب نیست!
    pause
    exit /b 1
)

echo.
echo 2. ایجاد محیط مجازی...
python -m venv venv
if %errorlevel% neq 0 (
    echo ❌ خطا در ایجاد محیط مجازی!
    pause
    exit /b 1
)

echo.
echo 3. نصب کتابخانه‌ها...
venv\Scripts\pip.exe install --upgrade pip
venv\Scripts\pip.exe install selenium

echo.
echo 4. ایجاد فایل requirements...
venv\Scripts\pip.exe freeze > requirements.txt

echo.
echo ✅ راه‌اندازی با موفقیت انجام شد!
echo.
echo 📋 مراحل بعدی:
echo 1. ChromeDriver را از https://chromedriver.chromium.org/ دانلود کنید
echo 2. ChromeDriver را در PATH قرار دهید یا در پوشه پروژه قرار دهید
echo 3. اطلاعات ورود Sanjab را در فایل sanjab_scraper.py تغییر دهید
echo 4. اسکریپت را اجرا کنید:
echo    venv\Scripts\python.exe sanjab_scraper.py
echo.
pause
