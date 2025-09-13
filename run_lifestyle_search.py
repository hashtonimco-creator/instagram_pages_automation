#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Custom script to search for lifestyle and women's style Instagram pages
using Sanjab platform with automatic credentials
"""

from sanjab_influencer_search import SanjabInfluencerSearch
from sanjab_analytics import SanjabAnalytics
import pandas as pd
from datetime import datetime

def main():
    """Main function to run lifestyle influencer search and analysis"""
    print("🚀 شروع جستجوی صفحات لایف استایل و سبک زندگی خانم‌ها")
    print("=" * 60)
    
    # اطلاعات ورود
    EMAIL = "payegan@gmail.com"
    PASSWORD = "3xdVgd8XiMvxMPj"
    
    print("🔐 ورود با اطلاعات ارائه شده...")
    
    # ایجاد نمونه جستجوگر
    searcher = SanjabInfluencerSearch()
    
    # جستجوی اینفلوئنسرهای مرتبط با لایف استایل و سبک زندگی خانم‌ها
    print("\n🔍 مرحله 1: جستجوی اینفلوئنسرهای لایف استایل")
    
    # فیلترهای جستجو برای لایف استایل و سبک زندگی خانم‌ها
    category = "مد و فشن"  # یا "سبک زندگی"
    follower_min = 1000  # حداقل 1000 فالوور
    follower_max = 1000000  # حداکثر 1 میلیون فالوور
    gender = "زن"  # جنسیت زن
    max_pages = 5  # 5 صفحه نتایج
    
    print(f"📂 دسته‌بندی: {category}")
    print(f"👥 بازه فالوور: {follower_min:,} تا {follower_max:,}")
    print(f"👤 جنسیت: {gender}")
    print(f"📄 تعداد صفحات: {max_pages}")
    
    # اجرای جستجو
    search_success = searcher.run_influencer_search(
        EMAIL, PASSWORD, category, follower_min, 
        follower_max, gender, max_pages, headless=False
    )
    
    if not search_success:
        print("❌ جستجو با خطا مواجه شد!")
        return False
    
    # پیدا کردن فایل نتایج جستجو
    import os
    search_files = [f for f in os.listdir('.') if f.startswith('influencers_search_results_') and f.endswith('.csv')]
    
    if not search_files:
        print("❌ فایل نتایج جستجو یافت نشد!")
        return False
    
    latest_search_file = sorted(search_files)[-1]
    print(f"\n📄 فایل نتایج جستجو: {latest_search_file}")
    
    # مرحله 2: تحلیل آمار اینفلوئنسرها
    print("\n📊 مرحله 2: تحلیل آمار اینفلوئنسرها")
    
    analyzer = SanjabAnalytics()
    analysis_success = analyzer.run_analysis(latest_search_file, EMAIL, PASSWORD, headless=False)
    
    if not analysis_success:
        print("❌ تحلیل آمار با خطا مواجه شد!")
        return False
    
    # پیدا کردن فایل نتایج تحلیل
    analytics_files = [f for f in os.listdir('.') if f.startswith('comprehensive_instagram_analytics_') and f.endswith('.csv')]
    
    if not analytics_files:
        print("❌ فایل نتایج تحلیل یافت نشد!")
        return False
    
    latest_analytics_file = sorted(analytics_files)[-1]
    print(f"\n📄 فایل نتایج تحلیل: {latest_analytics_file}")
    
    # مرحله 3: فیلتر و مرتب‌سازی بر اساس نرخ تعامل
    print("\n🔄 مرحله 3: فیلتر و مرتب‌سازی نتایج")
    
    try:
        # خواندن نتایج تحلیل
        df = pd.read_csv(latest_analytics_file, encoding='utf-8-sig')
        
        # فیلتر صفحات با نرخ تعامل معتبر
        df_filtered = df[df['engagement_rate'] != 'N/A'].copy()
        
        # تبدیل نرخ تعامل به عدد
        df_filtered['engagement_rate_numeric'] = pd.to_numeric(
            df_filtered['engagement_rate'], errors='coerce'
        )
        
        # حذف ردیف‌های بدون نرخ تعامل معتبر
        df_filtered = df_filtered.dropna(subset=['engagement_rate_numeric'])
        
        # مرتب‌سازی بر اساس نرخ تعامل (نزولی)
        df_sorted = df_filtered.sort_values('engagement_rate_numeric', ascending=False)
        
        # ذخیره نتایج نهایی
        final_filename = f'lifestyle_women_pages_by_engagement_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        df_sorted.to_csv(final_filename, index=False, encoding='utf-8-sig')
        
        print(f"✅ نتایج نهایی در فایل {final_filename} ذخیره شد")
        
        # نمایش نتایج
        print(f"\n📈 نتایج نهایی - {len(df_sorted)} صفحه لایف استایل مرتب‌سازی شده:")
        print("=" * 80)
        
        for i, (_, row) in enumerate(df_sorted.head(20).iterrows(), 1):
            engagement_rate = row['engagement_rate_numeric']
            page_name = row['page_name']
            
            print(f"{i:2d}. @{page_name:<25} | نرخ تعامل: {engagement_rate:.2f}%")
        
        if len(df_sorted) > 20:
            print(f"\n... و {len(df_sorted) - 20} صفحه دیگر")
        
        # نمایش آمار خلاصه
        print(f"\n📊 آمار خلاصه:")
        print(f"   تعداد کل صفحات تحلیل شده: {len(df)}")
        print(f"   صفحات با نرخ تعامل معتبر: {len(df_sorted)}")
        print(f"   بالاترین نرخ تعامل: {df_sorted['engagement_rate_numeric'].max():.2f}%")
        print(f"   کمترین نرخ تعامل: {df_sorted['engagement_rate_numeric'].min():.2f}%")
        print(f"   میانگین نرخ تعامل: {df_sorted['engagement_rate_numeric'].mean():.2f}%")
        
        return True
        
    except Exception as e:
        print(f"❌ خطا در پردازش نتایج: {str(e)}")
        return False

if __name__ == "__main__":
    success = main()
    
    if success:
        print("\n🎉 فرآیند با موفقیت تکمیل شد!")
        print("📄 فایل نتایج نهایی آماده است.")
    else:
        print("\n❌ فرآیند با خطا مواجه شد!")

