@echo off
echo 🎯 Sanjab Influencer Search - جستجوی پیشرفته اینفلوئنسرها
echo =========================================================

echo فعال‌سازی محیط مجازی...
call venv\Scripts\activate.bat

echo.
echo اجرای جستجوی اینفلوئنسرها...
python run_influencer_search.py

echo.
echo جستجو به پایان رسید.
pause
