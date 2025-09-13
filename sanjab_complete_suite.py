#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sanjab Complete Suite - مجموعه کامل ابزارهای Sanjab
شامل: جستجوی اینفلوئنسرها + تحلیل آمار
"""

from sanjab_influencer_search import SanjabInfluencerSearch
from sanjab_analytics import SanjabAnalytics
import os
import pandas as pd
from datetime import datetime

class SanjabCompleteSuite:
    def __init__(self):
        """مقداردهی اولیه"""
        self.email = None
        self.password = None
        
    def get_credentials(self):
        """دریافت اطلاعات ورود"""
        print("🔐 اطلاعات ورود Sanjab:")
        self.email = input("ایمیل: ").strip()
        self.password = input("رمز عبور: ").strip()
        
        if not self.email or not self.password:
            print("❌ اطلاعات ورود وارد نشده!")
            return False
        return True
    
    def search_influencers(self):
        """جستجوی اینفلوئنسرها"""
        print("\n🔍 مرحله 1: جستجوی اینفلوئنسرها")
        print("=" * 40)
        
        # دریافت فیلترهای جستجو
        print("⚙️ تنظیم فیلترهای جستجو:")
        category = input("دسته‌بندی (اختیاری): ").strip() or None
        follower_min = input("حداقل فالوور (اختیاری): ").strip() or None
        follower_max = input("حداکثر فالوور (اختیاری): ").strip() or None
        gender = input("جنسیت (اختیاری): ").strip() or None
        max_pages = input("حداکثر صفحات (پیش‌فرض: 3): ").strip() or "3"
        
        try:
            follower_min = int(follower_min) if follower_min else None
            follower_max = int(follower_max) if follower_max else None
            max_pages = int(max_pages) if max_pages else 3
        except ValueError:
            print("❌ مقادیر عددی نامعتبر!")
            return False
        
        # اجرای جستجو
        searcher = SanjabInfluencerSearch()
        success = searcher.run_influencer_search(
            self.email, self.password, category, follower_min, 
            follower_max, gender, max_pages, headless=False
        )
        
        if success:
            print("✅ جستجوی اینفلوئنسرها تکمیل شد")
            return True
        else:
            print("❌ جستجوی اینفلوئنسرها با خطا مواجه شد")
            return False
    
    def analyze_influencers(self, csv_file=None):
        """تحلیل آمار اینفلوئنسرها"""
        print("\n📊 مرحله 2: تحلیل آمار اینفلوئنسرها")
        print("=" * 40)
        
        # انتخاب فایل CSV
        if not csv_file:
            print("📁 انتخاب فایل CSV:")
            print("1. استفاده از فایل جستجوی اخیر")
            print("2. استفاده از فایل موجود")
            print("3. استفاده از فایل پیش‌فرض (instagram_pages.csv)")
            
            choice = input("انتخاب کنید (1/2/3): ").strip()
            
            if choice == "1":
                # پیدا کردن آخرین فایل جستجو
                csv_files = [f for f in os.listdir('.') if f.startswith('influencers_search_results_') and f.endswith('.csv')]
                if csv_files:
                    csv_file = sorted(csv_files)[-1]  # آخرین فایل
                    print(f"📄 استفاده از فایل: {csv_file}")
                else:
                    print("❌ فایل جستجوی اخیر یافت نشد!")
                    return False
            elif choice == "2":
                csv_file = input("نام فایل CSV: ").strip()
                if not os.path.exists(csv_file):
                    print("❌ فایل یافت نشد!")
                    return False
            else:
                csv_file = "instagram_pages.csv"
                if not os.path.exists(csv_file):
                    print("❌ فایل instagram_pages.csv یافت نشد!")
                    return False
        
        # اجرای تحلیل
        analyzer = SanjabAnalytics()
        success = analyzer.run_analysis(csv_file, self.email, self.password, headless=False)
        
        if success:
            print("✅ تحلیل آمار تکمیل شد")
            return True
        else:
            print("❌ تحلیل آمار با خطا مواجه شد")
            return False
    
    def combine_results(self):
        """ترکیب نتایج جستجو و تحلیل"""
        print("\n🔄 مرحله 3: ترکیب نتایج")
        print("=" * 40)
        
        try:
            # پیدا کردن فایل‌های اخیر
            search_files = [f for f in os.listdir('.') if f.startswith('influencers_search_results_') and f.endswith('.csv')]
            analytics_files = [f for f in os.listdir('.') if f.startswith('comprehensive_instagram_analytics_') and f.endswith('.csv')]
            
            if not search_files or not analytics_files:
                print("❌ فایل‌های لازم یافت نشدند!")
                return False
            
            # آخرین فایل‌ها
            latest_search = sorted(search_files)[-1]
            latest_analytics = sorted(analytics_files)[-1]
            
            print(f"📄 فایل جستجو: {latest_search}")
            print(f"📄 فایل تحلیل: {latest_analytics}")
            
            # خواندن فایل‌ها
            search_df = pd.read_csv(latest_search, encoding='utf-8-sig')
            analytics_df = pd.read_csv(latest_analytics, encoding='utf-8-sig')
            
            # ترکیب داده‌ها
            combined_df = pd.merge(
                search_df, 
                analytics_df, 
                on='page_name', 
                how='left'
            )
            
            # ذخیره فایل ترکیبی
            combined_filename = f'complete_analysis_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
            combined_df.to_csv(combined_filename, index=False, encoding='utf-8-sig')
            
            print(f"✅ فایل ترکیبی ایجاد شد: {combined_filename}")
            print(f"📊 تعداد رکوردها: {len(combined_df)}")
            
            # نمایش خلاصه
            print("\n📈 خلاصه نتایج:")
            print(f"   اینفلوئنسرهای یافت شده: {len(search_df)}")
            print(f"   اینفلوئنسرهای تحلیل شده: {len(analytics_df)}")
            print(f"   اینفلوئنسرهای ترکیبی: {len(combined_df)}")
            
            return True
            
        except Exception as e:
            print(f"❌ خطا در ترکیب نتایج: {str(e)}")
            return False
    
    def run_complete_workflow(self):
        """اجرای کامل فرآیند"""
        print("🚀 Sanjab Complete Suite - مجموعه کامل ابزارها")
        print("=" * 60)
        
        # دریافت اطلاعات ورود
        if not self.get_credentials():
            return False
        
        # انتخاب نوع اجرا
        print("\n🎯 انتخاب نوع اجرا:")
        print("1. جستجوی اینفلوئنسرها فقط")
        print("2. تحلیل آمار فقط")
        print("3. جستجو + تحلیل + ترکیب (کامل)")
        
        choice = input("انتخاب کنید (1/2/3): ").strip()
        
        if choice == "1":
            return self.search_influencers()
        elif choice == "2":
            return self.analyze_influencers()
        elif choice == "3":
            # اجرای کامل
            if self.search_influencers():
                if self.analyze_influencers():
                    return self.combine_results()
            return False
        else:
            print("❌ انتخاب نامعتبر!")
            return False

def main():
    """تابع اصلی"""
    suite = SanjabCompleteSuite()
    success = suite.run_complete_workflow()
    
    if success:
        print("\n🎉 فرآیند با موفقیت تکمیل شد!")
    else:
        print("\n❌ فرآیند با خطا مواجه شد!")

if __name__ == "__main__":
    main()
