@echo off
echo 🚀 اجرای Sanjab Instagram Analytics
echo ====================================

echo فعال‌سازی محیط مجازی...
call venv\Scripts\activate.bat

echo.
echo اجرای اسکریپت جامع...
python run_analytics.py

echo.
echo اسکریپت به پایان رسید.
pause
