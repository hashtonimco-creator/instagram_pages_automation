#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup script for Sanjab Instagram Analytics Scraper
"""

import subprocess
import sys
import os

def run_command(command):
    """اجرای دستور در terminal"""
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {command}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ خطا در اجرای دستور: {command}")
        print(f"خطا: {e.stderr}")
        return False

def main():
    print("🚀 راه‌اندازی پروژه Sanjab Instagram Analytics Scraper")
    print("=" * 60)
    
    # بررسی وجود Python
    print("1. بررسی Python...")
    if not run_command("python --version"):
        print("❌ Python نصب نیست!")
        return False
    
    # ایجاد محیط مجازی
    print("\n2. ایجاد محیط مجازی...")
    if not run_command("python -m venv venv"):
        print("❌ خطا در ایجاد محیط مجازی!")
        return False
    
    # فعال‌سازی محیط مجازی و نصب کتابخانه‌ها
    print("\n3. نصب کتابخانه‌ها...")
    if os.name == 'nt':  # Windows
        activate_cmd = "venv\\Scripts\\activate"
        pip_cmd = "venv\\Scripts\\pip"
    else:  # Linux/Mac
        activate_cmd = "source venv/bin/activate"
        pip_cmd = "venv/bin/pip"
    
    if not run_command(f"{pip_cmd} install --upgrade pip"):
        print("❌ خطا در به‌روزرسانی pip!")
        return False
    
    if not run_command(f"{pip_cmd} install selenium"):
        print("❌ خطا در نصب selenium!")
        return False
    
    # ایجاد فایل requirements
    print("\n4. ایجاد فایل requirements...")
    if not run_command(f"{pip_cmd} freeze > requirements.txt"):
        print("❌ خطا در ایجاد requirements.txt!")
        return False
    
    print("\n✅ راه‌اندازی با موفقیت انجام شد!")
    print("\n📋 مراحل بعدی:")
    print("1. ChromeDriver را از https://chromedriver.chromium.org/ دانلود کنید")
    print("2. ChromeDriver را در PATH قرار دهید یا در پوشه پروژه قرار دهید")
    print("3. اطلاعات ورود Sanjab را در فایل sanjab_scraper.py تغییر دهید")
    print("4. اسکریپت را اجرا کنید:")
    if os.name == 'nt':
        print("   venv\\Scripts\\python.exe sanjab_scraper.py")
    else:
        print("   venv/bin/python sanjab_scraper.py")
    
    return True

if __name__ == "__main__":
    main()
