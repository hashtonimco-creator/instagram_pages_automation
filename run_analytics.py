#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sanjab Instagram Analytics - اجرای ساده
"""

from sanjab_analytics import SanjabAnalytics
import os

def main():
    print("🎯 Sanjab Instagram Analytics")
    print("=" * 40)
    
    # بررسی وجود فایل CSV
    if not os.path.exists('instagram_pages.csv'):
        print("❌ فایل instagram_pages.csv یافت نشد!")
        return
    
    # تنظیمات (لطفاً اطلاعات خود را وارد کنید)
    EMAIL = input("ایمیل Sanjab: ").strip()
    PASSWORD = input("رمز عبور Sanjab: ").strip()
    
    if not EMAIL or not PASSWORD:
        print("❌ اطلاعات ورود وارد نشده!")
        return
    
    # ایجاد و اجرای تحلیل
    analyzer = SanjabAnalytics()
    success = analyzer.run_analysis('instagram_pages.csv', EMAIL, PASSWORD, headless=False)
    
    if success:
        print("\n🎉 تحلیل با موفقیت انجام شد!")
    else:
        print("\n❌ تحلیل با خطا مواجه شد!")

if __name__ == "__main__":
    main()
