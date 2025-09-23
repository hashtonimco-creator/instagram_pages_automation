#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sanjab Analytics Module

This module is designed for analyzing Instagram pages through the Sanjab platform.
"""

import pandas as pd
import time
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class SanjabAnalytics:
    """Sanjab page analysis class"""
    
    def __init__(self):
        self.driver = None
        self.wait = None
        
    def setup_driver(self, headless=False):
        """Setup Chrome WebDriver"""
        try:
            chrome_options = Options()
            if headless:
                chrome_options.add_argument("--headless")
            
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
            
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            self.wait = WebDriverWait(self.driver, 10)
            
            print("✅ Chrome WebDriver setup successful")
            return True
            
        except Exception as e:
            print(f"❌ Error setting up WebDriver: {str(e)}")
            return False
    
    def login(self, email, password):
        """Login to Sanjab"""
        try:
            print("🔐 Logging into Sanjab...")
            self.driver.get("https://app.sanjab.co/auth/login")
            
            # Enter email
            email_field = self.wait.until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            email_field.clear()
            email_field.send_keys(email)
            
            # Enter password
            password_field = self.driver.find_element(By.NAME, "password")
            password_field.clear()
            password_field.send_keys(password)
            
            # Click login button
            login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
            login_button.click()
            
            # Wait for successful login
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'navbar')]"))
            )
            
            print("✅ Successfully logged into Sanjab")
            return True
            
        except TimeoutException:
            print("❌ Login error: timeout")
            return False
        except Exception as e:
            print(f"❌ Login error: {str(e)}")
            return False
    
    def analyze_page(self, page_name):
        """Analyze a specific page"""
        try:
            print(f"📊 Analyzing page: {page_name}")
            
            # Search for page
            search_url = f"https://app.sanjab.co/search?q={page_name}"
            self.driver.get(search_url)
            
            # Wait for results to load
            time.sleep(3)
            
            # Click on first result
            first_result = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, '_item_')]"))
            )
            first_result.click()
            
            # Wait for analysis page to load
            time.sleep(5)
            
            # Extract information
            analytics_data = self.extract_analytics_data()
            
            return analytics_data
            
        except Exception as e:
            print(f"❌ Error analyzing page {page_name}: {str(e)}")
            return None
    
    def extract_analytics_data(self):
        """Extract analytics data"""
        try:
            data = {
                'page_name': '',
                'followers': 0,
                'engagement_rate': 0.0,
                'avg_likes': 0,
                'avg_comments': 0,
                'avg_shares': 0,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # Extract page name
            try:
                page_name_element = self.driver.find_element(By.XPATH, "//h1[contains(@class, 'page-title')]")
                data['page_name'] = page_name_element.text.strip()
            except NoSuchElementException:
                data['page_name'] = "Unknown"
            
            # Extract followers count
            try:
                followers_element = self.driver.find_element(By.XPATH, "//span[contains(text(), 'followers')]/preceding-sibling::span")
                followers_text = followers_element.text.strip()
                data['followers'] = self.parse_number(followers_text)
            except NoSuchElementException:
                data['followers'] = 0
            
            # Extract engagement rate
            try:
                engagement_element = self.driver.find_element(By.XPATH, "//span[contains(text(), 'engagement')]/following-sibling::span")
                engagement_text = engagement_element.text.strip().replace('%', '')
                data['engagement_rate'] = float(engagement_text)
            except NoSuchElementException:
                data['engagement_rate'] = 0.0
            
            # Extract average likes
            try:
                likes_element = self.driver.find_element(By.XPATH, "//span[contains(text(), 'likes')]/following-sibling::span")
                likes_text = likes_element.text.strip()
                data['avg_likes'] = self.parse_number(likes_text)
            except NoSuchElementException:
                data['avg_likes'] = 0
            
            # Extract average comments
            try:
                comments_element = self.driver.find_element(By.XPATH, "//span[contains(text(), 'comments')]/following-sibling::span")
                comments_text = comments_element.text.strip()
                data['avg_comments'] = self.parse_number(comments_text)
            except NoSuchElementException:
                data['avg_comments'] = 0
            
            return data
            
        except Exception as e:
            print(f"❌ Error extracting data: {str(e)}")
            return None
    
    def parse_number(self, text):
        """Convert text to number"""
        try:
            # Remove non-numeric characters
            clean_text = ''.join(filter(str.isdigit, text))
            if clean_text:
                return int(clean_text)
            return 0
        except:
            return 0
    
    def run_analysis(self, csv_file, email, password, headless=False):
        """Execute complete analysis"""
        try:
            print("🚀 Starting Instagram page analysis")
            print("=" * 50)
            
            # Setup WebDriver
            if not self.setup_driver(headless):
                return False
            
            # Login to Sanjab
            if not self.login(email, password):
                return False
            
            # Read CSV file
            if not os.path.exists(csv_file):
                print(f"❌ File {csv_file} not found!")
                return False
            
            df = pd.read_csv(csv_file, encoding='utf-8')
            print(f"📋 Number of pages to analyze: {len(df)}")
            
            # Analyze pages
            results = []
            for index, row in df.iterrows():
                page_name = row.get('page_name', '')
                if page_name:
                    print(f"\n📊 Analyzing page {index + 1}/{len(df)}: {page_name}")
                    
                    analytics_data = self.analyze_page(page_name)
                    if analytics_data:
                        results.append(analytics_data)
                    
                    # Short pause between requests
                    time.sleep(2)
            
            # Save results
            if results:
                results_df = pd.DataFrame(results)
                output_filename = f'analytics_results_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
                results_df.to_csv(output_filename, index=False, encoding='utf-8-sig')
                
                print(f"\n✅ Results saved to {output_filename}")
                print(f"📊 Number of pages analyzed: {len(results)}")
                
                return results_df
            else:
                print("❌ No results found!")
                return None
                
        except Exception as e:
            print(f"❌ Error in analysis execution: {str(e)}")
            return None
        finally:
            if self.driver:
                self.driver.quit()
                print("🔚 Browser closed")

if __name__ == "__main__":
    # Usage example
    analyzer = SanjabAnalytics()
    results = analyzer.run_analysis(
        csv_file="data/sample_pages.csv",
        email="payegan@gmail.com",
        password="3xdVgd8XiMvxMPj",
        headless=False
    )

