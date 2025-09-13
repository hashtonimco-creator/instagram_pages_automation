#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sanjab Influencer Search - اجرای ساده جستجوی اینفلوئنسرها
"""

from sanjab_influencer_search import SanjabInfluencerSearch
import os

def main():
    print("🎯 Sanjab Influencer Search - جستجوی پیشرفته اینفلوئنسرها")
    print("=" * 60)
    
    # دریافت اطلاعات ورود
    email = input("ایمیل Sanjab: ").strip()
    password = input("رمز عبور Sanjab: ").strip()
    
    if not email or not password:
        print("❌ اطلاعات ورود وارد نشده!")
        return
    
    # تنظیمات پیش‌فرض
    print("\n⚙️ تنظیم فیلترهای جستجو:")
    print("(برای رد کردن هر فیلتر، Enter بزنید)")
    
    # فیلترهای قابل تنظیم
    category = input("دسته‌بندی (مثال: مد و فشن، ورزش، تکنولوژی): ").strip() or None
    follower_min = input("حداقل تعداد فالوور: ").strip() or None
    follower_max = input("حداکثر تعداد فالوور: ").strip() or None
    gender = input("جنسیت (مرد، زن): ").strip() or None
    
    # تنظیمات پیشرفته
    print("\n🔧 تنظیمات پیشرفته:")
    max_pages = input("حداکثر تعداد صفحات (پیش‌فرض: 5): ").strip() or "5"
    headless = input("اجرای بدون نمایش مرورگر؟ (y/n، پیش‌فرض: n): ").strip().lower() == 'y'
    
    # تبدیل به عدد
    try:
        follower_min = int(follower_min) if follower_min else None
        follower_max = int(follower_max) if follower_max else None
        max_pages = int(max_pages) if max_pages else 5
    except ValueError:
        print("❌ مقادیر عددی نامعتبر!")
        return
    
    # نمایش تنظیمات
    print("\n📋 تنظیمات انتخاب شده:")
    print(f"   دسته‌بندی: {category or 'همه'}")
    print(f"   بازه فالوور: {follower_min or 'نامحدود'} - {follower_max or 'نامحدود'}")
    print(f"   جنسیت: {gender or 'همه'}")
    print(f"   حداکثر صفحات: {max_pages}")
    print(f"   حالت headless: {'بله' if headless else 'خیر'}")
    
    # تایید اجرا
    confirm = input("\nآیا می‌خواهید جستجو را شروع کنید؟ (y/n): ").strip().lower()
    if confirm != 'y':
        print("❌ جستجو لغو شد!")
        return
    
    # ایجاد و اجرای جستجو
    searcher = SanjabInfluencerSearch()
    success = searcher.run_influencer_search(
        email, password, category, follower_min, 
        follower_max, gender, max_pages, headless
    )
    
    if success:
        print("\n🎉 جستجوی اینفلوئنسرها با موفقیت انجام شد!")
        print("📁 فایل CSV با لیست اینفلوئنسرها ایجاد شد")
    else:
        print("\n❌ جستجو با خطا مواجه شد!")

if __name__ == "__main__":
    main()
