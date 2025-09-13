#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sanjab Instagram Analytics - Comprehensive Analytics Tool
ابزار جامع تحلیل آمار پیج‌های اینستاگرام از Sanjab
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import csv
import pandas as pd
from datetime import datetime
import time
import json
import os

class SanjabAnalytics:
    def __init__(self):
        """مقداردهی اولیه کلاس"""
        self.driver = None
        self.results = []
        self.pages_data = []
        
    def setup_driver(self, headless=False):
        """راه‌اندازی ChromeDriver با تنظیمات بهینه"""
        print("🔧 راه‌اندازی ChromeDriver...")
        
        chrome_options = Options()
        if headless:
            chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        
        try:
            self.driver = webdriver.Chrome(options=chrome_options)
            print("✅ ChromeDriver راه‌اندازی شد")
            return True
        except Exception as e:
            print(f"❌ خطا در راه‌اندازی ChromeDriver: {str(e)}")
            return False
    
    def login_to_sanjab(self, email, password):
        """ورود به Sanjab"""
        print("🔐 ورود به Sanjab...")
        
        try:
            # رفتن به صفحه ورود
            self.driver.get("https://app.sanjab.co/auth/login")
            time.sleep(3)

            # وارد کردن اطلاعات ورود
            username_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            password_field = self.driver.find_element(By.NAME, "password")
            login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

            username_field.send_keys(email)
            password_field.send_keys(password)
            login_button.click()

            # انتظار برای لود شدن صفحه اصلی
            time.sleep(5)
            print("✅ ورود موفقیت‌آمیز!")
            return True
            
        except Exception as e:
            print(f"❌ خطا در ورود: {str(e)}")
            return False
    
    def search_and_analyze_page(self, page_name):
        """جستجو و تحلیل یک پیج"""
        print(f"🔍 تحلیل پیج: {page_name}")
        
        try:
            # جستجوی پیج
            search_box = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
            )
            
            search_box.clear()
            search_box.send_keys(page_name)
            search_box.send_keys(Keys.RETURN)
            time.sleep(5)
            
            # استخراج آمارهای جامع
            stats = self.extract_comprehensive_stats(page_name)
            
            if stats:
                self.results.append(stats)
                print(f"✅ آمار {page_name} استخراج شد")
                return True
            else:
                print(f"❌ خطا در استخراج آمار {page_name}")
                return False
                
        except Exception as e:
            print(f"❌ خطا در تحلیل {page_name}: {str(e)}")
            return False
    
    def extract_comprehensive_stats(self, page_name):
        """استخراج آمارهای جامع از صفحه"""
        try:
            # انتظار برای لود شدن آمار
            time.sleep(3)
            
            # استخراج آمارهای مختلف
            stats = {
                'page_name': page_name,
                'engagement_rate': self.extract_metric("نرخ تعامل"),
                'engagement_rate_percentile': self.extract_metric("خوب"),
                'better_than_percent': self.extract_metric("بهتر از"),
                'similar_pages_percent': self.extract_metric("پیج‌های مشابه"),
                'likes_per_post': self.extract_metric("لایک به ازای هر پست"),
                'comments_per_post': self.extract_metric("کامنت به ازای هر پست"),
                'views_to_follower_ratio': self.extract_metric("نسبت بازدید به فالوور"),
                'likes_to_follower_ratio': self.extract_metric("نسبت لایک به فالوور"),
                'average_reel_views': self.extract_metric("میانگین بازدید هر Reel"),
                'average_shares': self.extract_metric("میانگین share"),
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            return stats
            
        except Exception as e:
            print(f"❌ خطا در استخراج آمار: {str(e)}")
            return None
    
    def extract_metric(self, metric_name):
        """استخراج یک متریک خاص"""
        try:
            # جستجوی متریک با XPath های مختلف
            xpath_patterns = [
                f"//div[contains(text(),'{metric_name}')]/following-sibling::div",
                f"//span[contains(text(),'{metric_name}')]/following-sibling::span",
                f"//td[contains(text(),'{metric_name}')]/following-sibling::td",
                f"//*[contains(text(),'{metric_name}')]/../*[2]"
            ]
            
            for xpath in xpath_patterns:
                try:
                    element = self.driver.find_element(By.XPATH, xpath)
                    value = element.text.strip()
                    if value:
                        return self.clean_numeric_value(value)
                except:
                    continue
            
            # اگر پیدا نشد، مقدار پیش‌فرض برگردان
            return "N/A"
            
        except Exception as e:
            return "N/A"
    
    def clean_numeric_value(self, value):
        """تمیز کردن مقادیر عددی"""
        if not value or value == "N/A":
            return "N/A"
        
        # حذف کاراکترهای اضافی
        cleaned = value.replace(",", "").replace("٪", "").replace("%", "").strip()
        
        # تبدیل به عدد اگر ممکن باشد
        try:
            if cleaned.replace(".", "").isdigit():
                return float(cleaned)
            else:
                return cleaned
        except:
            return value
    
    def read_pages_from_csv(self, filename):
        """خواندن لیست پیج‌ها از فایل CSV"""
        pages = []
        try:
            with open(filename, 'r', encoding='utf-8-sig') as file:
                csv_reader = csv.reader(file)
                pages = [row[0] for row in csv_reader if row and row[0].strip()]
            print(f"📋 {len(pages)} پیج از فایل {filename} خوانده شد")
            return pages
        except Exception as e:
            print(f"❌ خطا در خواندن فایل CSV: {str(e)}")
            return []
    
    def save_comprehensive_results(self, filename=None):
        """ذخیره نتایج جامع در فایل CSV"""
        if not filename:
            filename = f'comprehensive_instagram_analytics_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        
        try:
            if not self.results:
                print("❌ هیچ داده‌ای برای ذخیره وجود ندارد")
                return False
            
            # ایجاد DataFrame
            df = pd.DataFrame(self.results)
            
            # ذخیره در CSV
            df.to_csv(filename, index=False, encoding='utf-8-sig')
            
            print(f"✅ نتایج جامع در فایل {filename} ذخیره شد")
            print(f"📊 تعداد پیج‌های تحلیل شده: {len(self.results)}")
            
            # نمایش خلاصه آمار
            self.display_summary_stats(df)
            
            return True
            
        except Exception as e:
            print(f"❌ خطا در ذخیره نتایج: {str(e)}")
            return False
    
    def display_summary_stats(self, df):
        """نمایش خلاصه آمار"""
        print("\n📈 خلاصه آمار:")
        print("=" * 50)
        
        numeric_columns = ['engagement_rate', 'likes_per_post', 'comments_per_post', 
                          'average_reel_views', 'average_shares']
        
        for col in numeric_columns:
            if col in df.columns:
                try:
                    # تبدیل به عدد و محاسبه آمار
                    numeric_data = pd.to_numeric(df[col], errors='coerce')
                    if not numeric_data.isna().all():
                        print(f"{col}:")
                        print(f"  میانگین: {numeric_data.mean():.2f}")
                        print(f"  حداکثر: {numeric_data.max():.2f}")
                        print(f"  حداقل: {numeric_data.min():.2f}")
                except:
                    pass
    
    def run_analysis(self, csv_file, email, password, headless=False):
        """اجرای تحلیل کامل"""
        print("🚀 شروع تحلیل جامع Sanjab Instagram Analytics")
        print("=" * 60)
        
        # راه‌اندازی ChromeDriver
        if not self.setup_driver(headless):
            return False
        
        try:
            # ورود به Sanjab
            if not self.login_to_sanjab(email, password):
                return False
            
            # خواندن لیست پیج‌ها
            pages = self.read_pages_from_csv(csv_file)
            if not pages:
                return False
            
            # تحلیل هر پیج
            successful_analyses = 0
            for i, page in enumerate(pages, 1):
                print(f"\n📊 تحلیل {i}/{len(pages)}: {page}")
                
                if self.search_and_analyze_page(page):
                    successful_analyses += 1
                
                # مکث بین درخواست‌ها
                time.sleep(3)
            
            print(f"\n✅ تحلیل {successful_analyses} از {len(pages)} پیج موفق بود")
            
            # ذخیره نتایج
            if self.results:
                self.save_comprehensive_results()
                return True
            else:
                print("❌ هیچ نتیجه‌ای برای ذخیره وجود ندارد")
                return False
                
        except Exception as e:
            print(f"❌ خطا در اجرای تحلیل: {str(e)}")
            return False
        finally:
            if self.driver:
                self.driver.quit()
                print("🔒 مرورگر بسته شد")

def main():
    """تابع اصلی"""
    print("🎯 Sanjab Instagram Analytics - ابزار جامع تحلیل")
    print("=" * 60)
    
    # تنظیمات
    EMAIL = "payegan@gmail.com"  # ایمیل خود را وارد کنید
    PASSWORD = "3xdVgd8XiMvxMPj"  # رمز عبور خود را وارد کنید
    CSV_FILE = "instagram_pages.csv"
    
    # ایجاد نمونه از کلاس
    analyzer = SanjabAnalytics()
    
    # اجرای تحلیل
    success = analyzer.run_analysis(CSV_FILE, EMAIL, PASSWORD, headless=False)
    
    if success:
        print("\n🎉 تحلیل با موفقیت به پایان رسید!")
    else:
        print("\n❌ تحلیل با خطا مواجه شد!")

if __name__ == "__main__":
    main()
