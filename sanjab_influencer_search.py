#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sanjab Influencer Search - جستجوی پیشرفته اینفلوئنسرها
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import csv
import pandas as pd
from datetime import datetime
import time
import json

class SanjabInfluencerSearch:
    def __init__(self):
        """مقداردهی اولیه کلاس"""
        self.driver = None
        self.influencers = []
        
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
    
    def navigate_to_advanced_search(self):
        """رفتن به صفحه جستجوی پیشرفته"""
        print("🔍 رفتن به صفحه جستجوی پیشرفته...")
        
        try:
            self.driver.get("https://app.sanjab.co/search/advance")
            time.sleep(3)
            print("✅ صفحه جستجوی پیشرفته بارگذاری شد")
            return True
        except Exception as e:
            print(f"❌ خطا در بارگذاری صفحه جستجو: {str(e)}")
            return False
    
    def set_search_filters(self, category=None, follower_min=None, follower_max=None, gender=None):
        """تنظیم فیلترهای جستجو"""
        print("⚙️ تنظیم فیلترهای جستجو...")
        
        try:
            # تنظیم دسته‌بندی
            if category:
                print(f"📂 تنظیم دسته‌بندی: {category}")
                category_select = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='category']"))
                )
                select_category = Select(category_select)
                select_category.select_by_visible_text(category)
                time.sleep(1)
            
            # تنظیم بازه فالوور
            if follower_min:
                print(f"👥 حداقل فالوور: {follower_min}")
                follower_min_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='follower_min']")
                follower_min_input.clear()
                follower_min_input.send_keys(str(follower_min))
                time.sleep(1)
            
            if follower_max:
                print(f"👥 حداکثر فالوور: {follower_max}")
                follower_max_input = self.driver.find_element(By.CSS_SELECTOR, "input[name='follower_max']")
                follower_max_input.clear()
                follower_max_input.send_keys(str(follower_max))
                time.sleep(1)
            
            # تنظیم جنسیت
            if gender:
                print(f"👤 جنسیت: {gender}")
                gender_select = self.driver.find_element(By.CSS_SELECTOR, "select[name='gender']")
                select_gender = Select(gender_select)
                select_gender.select_by_visible_text(gender)
                time.sleep(1)
            
            # تنظیم مرتب‌سازی بر اساس نرخ تعامل (نزولی)
            print("📊 تنظیم مرتب‌سازی بر اساس نرخ تعامل (نزولی)")
            sort_select = self.driver.find_element(By.CSS_SELECTOR, "select[name='sort']")
            select_sort = Select(sort_select)
            select_sort.select_by_visible_text("نرخ تعامل (نزولی)")
            time.sleep(1)
            
            print("✅ فیلترهای جستجو تنظیم شدند")
            return True
            
        except Exception as e:
            print(f"❌ خطا در تنظیم فیلترها: {str(e)}")
            return False
    
    def execute_search(self):
        """اجرای جستجو"""
        print("🔍 اجرای جستجو...")
        
        try:
            # کلیک روی دکمه جستجو
            search_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
            )
            search_button.click()
            
            # انتظار برای لود شدن نتایج
            time.sleep(5)
            print("✅ جستجو اجرا شد")
            return True
            
        except Exception as e:
            print(f"❌ خطا در اجرای جستجو: {str(e)}")
            return False
    
    def extract_influencers_from_results(self):
        """استخراج لیست اینفلوئنسرها از نتایج"""
        print("📋 استخراج لیست اینفلوئنسرها...")
        
        try:
            # انتظار برای لود شدن نتایج
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".influencer-card, .result-item, .profile-card"))
            )
            
            # استخراج اینفلوئنسرها با XPath های مختلف
            influencer_selectors = [
                "//div[contains(@class, 'influencer')]//a[contains(@href, 'instagram')]",
                "//div[contains(@class, 'result')]//a[contains(@href, 'instagram')]",
                "//div[contains(@class, 'profile')]//a[contains(@href, 'instagram')]",
                "//a[contains(@href, 'instagram.com')]",
                "//div[contains(@class, 'card')]//h3//a",
                "//div[contains(@class, 'item')]//a[contains(text(), '@')]"
            ]
            
            influencers = set()  # استفاده از set برای جلوگیری از تکرار
            
            for selector in influencer_selectors:
                try:
                    elements = self.driver.find_elements(By.XPATH, selector)
                    for element in elements:
                        # استخراج نام اینفلوئنسر
                        influencer_name = self.extract_influencer_name(element)
                        if influencer_name and influencer_name not in influencers:
                            influencers.add(influencer_name)
                            print(f"✅ اینفلوئنسر یافت شد: {influencer_name}")
                except:
                    continue
            
            self.influencers = list(influencers)
            print(f"📊 تعداد کل اینفلوئنسرهای یافت شده: {len(self.influencers)}")
            return True
            
        except Exception as e:
            print(f"❌ خطا در استخراج اینفلوئنسرها: {str(e)}")
            return False
    
    def extract_influencer_name(self, element):
        """استخراج نام اینفلوئنسر از عنصر"""
        try:
            # روش‌های مختلف استخراج نام
            methods = [
                lambda: element.text.strip(),
                lambda: element.get_attribute('href').split('/')[-1] if element.get_attribute('href') else None,
                lambda: element.get_attribute('title'),
                lambda: element.find_element(By.TAG_NAME, 'img').get_attribute('alt') if element.find_element(By.TAG_NAME, 'img') else None
            ]
            
            for method in methods:
                try:
                    name = method()
                    if name and name.startswith('@'):
                        return name[1:]  # حذف @ از ابتدا
                    elif name and not name.startswith('http'):
                        return name
                except:
                    continue
            
            return None
            
        except Exception as e:
            return None
    
    def load_more_results(self, max_pages=5):
        """بارگذاری نتایج بیشتر"""
        print("📄 بارگذاری نتایج بیشتر...")
        
        for page in range(max_pages):
            try:
                # جستجوی دکمه "بیشتر" یا "صفحه بعد"
                load_more_selectors = [
                    "//button[contains(text(), 'بیشتر')]",
                    "//button[contains(text(), 'صفحه بعد')]",
                    "//a[contains(text(), 'بعدی')]",
                    "//button[contains(@class, 'load-more')]",
                    "//button[contains(@class, 'next')]"
                ]
                
                load_more_button = None
                for selector in load_more_selectors:
                    try:
                        load_more_button = self.driver.find_element(By.XPATH, selector)
                        if load_more_button.is_enabled():
                            break
                    except:
                        continue
                
                if load_more_button and load_more_button.is_enabled():
                    print(f"📄 بارگذاری صفحه {page + 2}...")
                    self.driver.execute_script("arguments[0].click();", load_more_button)
                    time.sleep(3)
                    
                    # استخراج اینفلوئنسرهای جدید
                    self.extract_influencers_from_results()
                else:
                    print("✅ تمام نتایج بارگذاری شدند")
                    break
                    
            except Exception as e:
                print(f"⚠️ خطا در بارگذاری صفحه {page + 2}: {str(e)}")
                break
    
    def save_influencers_to_csv(self, filename=None):
        """ذخیره لیست اینفلوئنسرها در فایل CSV"""
        if not filename:
            filename = f'influencers_search_results_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
        
        try:
            if not self.influencers:
                print("❌ هیچ اینفلوئنسری برای ذخیره وجود ندارد")
                return False
            
            # ایجاد DataFrame
            df = pd.DataFrame({
                'page_name': self.influencers,
                'source': 'sanjab_search',
                'discovered_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            
            # ذخیره در CSV
            df.to_csv(filename, index=False, encoding='utf-8-sig')
            
            print(f"✅ لیست {len(self.influencers)} اینفلوئنسر در فایل {filename} ذخیره شد")
            
            # نمایش نمونه
            print("\n📋 نمونه اینفلوئنسرهای یافت شده:")
            for i, influencer in enumerate(self.influencers[:10], 1):
                print(f"   {i}. {influencer}")
            
            if len(self.influencers) > 10:
                print(f"   ... و {len(self.influencers) - 10} اینفلوئنسر دیگر")
            
            return True
            
        except Exception as e:
            print(f"❌ خطا در ذخیره فایل CSV: {str(e)}")
            return False
    
    def run_influencer_search(self, email, password, category=None, follower_min=None, 
                            follower_max=None, gender=None, max_pages=5, headless=False):
        """اجرای جستجوی کامل اینفلوئنسرها"""
        print("🚀 شروع جستجوی پیشرفته اینفلوئنسرها")
        print("=" * 60)
        
        # راه‌اندازی ChromeDriver
        if not self.setup_driver(headless):
            return False
        
        try:
            # ورود به Sanjab
            if not self.login_to_sanjab(email, password):
                return False
            
            # رفتن به صفحه جستجوی پیشرفته
            if not self.navigate_to_advanced_search():
                return False
            
            # تنظیم فیلترها
            if not self.set_search_filters(category, follower_min, follower_max, gender):
                return False
            
            # اجرای جستجو
            if not self.execute_search():
                return False
            
            # استخراج اینفلوئنسرها
            if not self.extract_influencers_from_results():
                return False
            
            # بارگذاری نتایج بیشتر
            self.load_more_results(max_pages)
            
            # ذخیره نتایج
            if self.influencers:
                self.save_influencers_to_csv()
                return True
            else:
                print("❌ هیچ اینفلوئنسری یافت نشد!")
                return False
                
        except Exception as e:
            print(f"❌ خطا در اجرای جستجو: {str(e)}")
            return False
        finally:
            if self.driver:
                self.driver.quit()
                print("🔒 مرورگر بسته شد")

def main():
    """تابع اصلی"""
    print("🎯 Sanjab Influencer Search - جستجوی پیشرفته اینفلوئنسرها")
    print("=" * 60)
    
    # دریافت اطلاعات ورود
    email = input("ایمیل Sanjab: ").strip()
    password = input("رمز عبور Sanjab: ").strip()
    
    if not email or not password:
        print("❌ اطلاعات ورود وارد نشده!")
        return
    
    # دریافت فیلترهای جستجو
    print("\n⚙️ تنظیم فیلترهای جستجو:")
    print("(برای رد کردن هر فیلتر، Enter بزنید)")
    
    category = input("دسته‌بندی (مثال: مد و فشن، ورزش، تکنولوژی): ").strip() or None
    follower_min = input("حداقل تعداد فالوور: ").strip() or None
    follower_max = input("حداکثر تعداد فالوور: ").strip() or None
    gender = input("جنسیت (مرد، زن): ").strip() or None
    max_pages = input("حداکثر تعداد صفحات برای بارگذاری (پیش‌فرض: 5): ").strip() or "5"
    
    # تبدیل به عدد
    try:
        follower_min = int(follower_min) if follower_min else None
        follower_max = int(follower_max) if follower_max else None
        max_pages = int(max_pages) if max_pages else 5
    except ValueError:
        print("❌ مقادیر عددی نامعتبر!")
        return
    
    # ایجاد و اجرای جستجو
    searcher = SanjabInfluencerSearch()
    success = searcher.run_influencer_search(
        email, password, category, follower_min, 
        follower_max, gender, max_pages, headless=False
    )
    
    if success:
        print("\n🎉 جستجوی اینفلوئنسرها با موفقیت انجام شد!")
    else:
        print("\n❌ جستجو با خطا مواجه شد!")

if __name__ == "__main__":
    main()
