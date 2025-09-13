#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Automatic Instagram Analytics Runner
اجرای خودکار تحلیل آمار اینستاگرام
"""

from sanjab_analytics import SanjabAnalytics
import pandas as pd
from datetime import datetime

def main():
    """Main function to run analytics automatically"""
    print("🚀 شروع تحلیل خودکار آمار اینستاگرام")
    print("=" * 60)
    
    # اطلاعات ورود
    EMAIL = "payegan@gmail.com"
    PASSWORD = "3xdVgd8XiMvxMPj"
    CSV_FILE = "lifestyle_pages.csv"
    
    print("🔐 استفاده از اطلاعات ورود ارائه شده...")
    print(f"📄 فایل صفحات: {CSV_FILE}")
    
    # ایجاد نمونه تحلیلگر
    analyzer = SanjabAnalytics()
    
    # اجرای تحلیل
    print("\n📊 شروع تحلیل آمار...")
    success = analyzer.run_analysis(CSV_FILE, EMAIL, PASSWORD, headless=False)
    
    if not success:
        print("❌ تحلیل با خطا مواجه شد!")
        return False
    
    # پردازش نتایج
    print("\n🔄 پردازش و مرتب‌سازی نتایج...")
    
    try:
        # پیدا کردن فایل نتایج
        import os
        analytics_files = [f for f in os.listdir('.') if f.startswith('comprehensive_instagram_analytics_') and f.endswith('.csv')]
        
        if not analytics_files:
            print("❌ فایل نتایج تحلیل یافت نشد!")
            return False
        
        latest_analytics_file = sorted(analytics_files)[-1]
        print(f"📄 فایل نتایج: {latest_analytics_file}")
        
        # خواندن نتایج
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
        final_filename = f'lifestyle_pages_by_engagement_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        df_sorted.to_csv(final_filename, index=False, encoding='utf-8-sig')
        
        print(f"✅ نتایج نهایی در فایل {final_filename} ذخیره شد")
        
        # نمایش نتایج
        print(f"\n📈 نتایج نهایی - {len(df_sorted)} صفحه لایف استایل مرتب‌سازی شده:")
        print("=" * 80)
        
        for i, (_, row) in enumerate(df_sorted.iterrows(), 1):
            engagement_rate = row['engagement_rate_numeric']
            page_name = row['page_name']
            
            print(f"{i:2d}. @{page_name:<25} | نرخ تعامل: {engagement_rate:.2f}%")
        
        # نمایش آمار خلاصه
        print(f"\n📊 آمار خلاصه:")
        print(f"   تعداد کل صفحات تحلیل شده: {len(df)}")
        print(f"   صفحات با نرخ تعامل معتبر: {len(df_sorted)}")
        
        if len(df_sorted) > 0:
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

