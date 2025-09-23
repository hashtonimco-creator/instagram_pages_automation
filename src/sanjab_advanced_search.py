#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sanjab Advanced Search Module

This module is designed for advanced search functionality on Sanjab platform
with specific filters for extracting top pages by engagement rate.
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
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class SanjabAdvancedSearch:
    """Sanjab advanced search class for extracting top pages by engagement rate"""
    
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
            self.wait = WebDriverWait(self.driver, 15)
            
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
    
    def navigate_to_advanced_search(self):
        """Navigate to advanced search page"""
        try:
            print("🔍 Navigating to advanced search...")
            self.driver.get("https://app.sanjab.co/search/advance")
            
            # Wait for page to load
            self.wait.until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            print("✅ Advanced search page loaded")
            return True
            
        except Exception as e:
            print(f"❌ Error navigating to advanced search: {str(e)}")
            return False
    
    def apply_filters(self, categories, gender, min_followers, max_followers):
        """Apply search filters on the advanced search page"""
        try:
            print("⚙️ Applying search filters...")
            
            # Wait for filters to load
            time.sleep(3)
            
            # Select categories
            if categories:
                print(f"📂 Selecting categories: {', '.join(categories)}")
                for category in categories:
                    try:
                        # Look for category checkboxes or dropdown options
                        category_element = self.driver.find_element(
                            By.XPATH, 
                            f"//label[contains(text(), '{category}')]//input[@type='checkbox'] | //option[contains(text(), '{category}')]"
                        )
                        if not category_element.is_selected():
                            category_element.click()
                        time.sleep(1)
                    except NoSuchElementException:
                        print(f"⚠️ Category '{category}' not found, trying alternative selectors...")
                        # Try alternative selectors
                        try:
                            category_element = self.driver.find_element(
                                By.XPATH, 
                                f"//*[contains(text(), '{category}')]//preceding-sibling::input[@type='checkbox'] | //*[contains(text(), '{category}')]//following-sibling::input[@type='checkbox']"
                            )
                            if not category_element.is_selected():
                                category_element.click()
                        except NoSuchElementException:
                            print(f"⚠️ Could not find category: {category}")
            
            # Select gender
            if gender:
                print(f"👤 Selecting gender: {gender}")
                try:
                    gender_element = self.driver.find_element(
                        By.XPATH, 
                        f"//label[contains(text(), '{gender}')]//input[@type='radio'] | //option[contains(text(), '{gender}')]"
                    )
                    gender_element.click()
                    time.sleep(1)
                except NoSuchElementException:
                    print(f"⚠️ Gender '{gender}' not found, trying alternative selectors...")
                    try:
                        gender_element = self.driver.find_element(
                            By.XPATH, 
                            f"//*[contains(text(), '{gender}')]//preceding-sibling::input[@type='radio'] | //*[contains(text(), '{gender}')]//following-sibling::input[@type='radio']"
                        )
                        gender_element.click()
                    except NoSuchElementException:
                        print(f"⚠️ Could not find gender: {gender}")
            
            # Set follower range
            if min_followers and max_followers:
                print(f"👥 Setting follower range: {min_followers:,} - {max_followers:,}")
                try:
                    # Look for follower range inputs
                    min_followers_input = self.driver.find_element(
                        By.XPATH, 
                        "//input[contains(@placeholder, 'min') or contains(@name, 'min') or contains(@id, 'min')]"
                    )
                    min_followers_input.clear()
                    min_followers_input.send_keys(str(min_followers))
                    
                    max_followers_input = self.driver.find_element(
                        By.XPATH, 
                        "//input[contains(@placeholder, 'max') or contains(@name, 'max') or contains(@id, 'max')]"
                    )
                    max_followers_input.clear()
                    max_followers_input.send_keys(str(max_followers))
                    
                    time.sleep(1)
                except NoSuchElementException:
                    print("⚠️ Follower range inputs not found, trying alternative selectors...")
                    try:
                        # Try alternative selectors for follower inputs
                        follower_inputs = self.driver.find_elements(
                            By.XPATH, 
                            "//input[@type='number'] | //input[contains(@class, 'follower')] | //input[contains(@class, 'range')]"
                        )
                        if len(follower_inputs) >= 2:
                            follower_inputs[0].clear()
                            follower_inputs[0].send_keys(str(min_followers))
                            follower_inputs[1].clear()
                            follower_inputs[1].send_keys(str(max_followers))
                    except Exception as e:
                        print(f"⚠️ Could not set follower range: {str(e)}")
            
            print("✅ Filters applied successfully")
            return True
            
        except Exception as e:
            print(f"❌ Error applying filters: {str(e)}")
            return False
    
    def execute_search(self):
        """Execute the search with applied filters"""
        try:
            print("🔍 Executing search...")
            
            # Look for search button
            search_button = self.driver.find_element(
                By.XPATH, 
                "//button[contains(text(), 'Search') or contains(text(), 'جستجو') or contains(@class, 'search')]"
            )
            search_button.click()
            
            # Wait for results to load
            self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'result') or contains(@class, 'item')]"))
            )
            
            print("✅ Search executed successfully")
            return True
            
        except Exception as e:
            print(f"❌ Error executing search: {str(e)}")
            return False
    
    def extract_page_data(self, page_element):
        """Extract data from a single page element"""
        try:
            data = {
                'page_name': '',
                'username': '',
                'followers': 0,
                'engagement_rate': 0.0,
                'description': '',
                'category': '',
                'verified': False,
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # Extract page name/username
            try:
                name_element = page_element.find_element(
                    By.XPATH, 
                    ".//h3 | .//h4 | .//div[contains(@class, 'name')] | .//div[contains(@class, 'title')]"
                )
                data['page_name'] = name_element.text.strip()
                data['username'] = data['page_name'].replace('@', '')
            except NoSuchElementException:
                data['page_name'] = "Unknown"
                data['username'] = "unknown"
            
            # Extract followers count
            try:
                followers_element = page_element.find_element(
                    By.XPATH, 
                    ".//span[contains(text(), 'followers') or contains(text(), 'فالوور')] | .//div[contains(@class, 'followers')]"
                )
                followers_text = followers_element.text.strip()
                data['followers'] = self.parse_number(followers_text)
            except NoSuchElementException:
                data['followers'] = 0
            
            # Extract engagement rate
            try:
                engagement_element = page_element.find_element(
                    By.XPATH, 
                    ".//span[contains(text(), '%')] | .//div[contains(@class, 'engagement')]"
                )
                engagement_text = engagement_element.text.strip().replace('%', '')
                data['engagement_rate'] = float(engagement_text)
            except NoSuchElementException:
                data['engagement_rate'] = 0.0
            
            # Extract description
            try:
                desc_element = page_element.find_element(
                    By.XPATH, 
                    ".//p | .//div[contains(@class, 'description')] | .//div[contains(@class, 'bio')]"
                )
                data['description'] = desc_element.text.strip()
            except NoSuchElementException:
                data['description'] = ""
            
            # Check if verified
            try:
                verified_element = page_element.find_element(
                    By.XPATH, 
                    ".//i[contains(@class, 'verified')] | .//span[contains(@class, 'verified')] | .//*[contains(text(), '✓')]"
                )
                data['verified'] = True
            except NoSuchElementException:
                data['verified'] = False
            
            return data
            
        except Exception as e:
            print(f"❌ Error extracting page data: {str(e)}")
            return None
    
    def parse_number(self, text):
        """Convert text to number"""
        try:
            # Remove non-numeric characters except decimal point
            clean_text = ''.join(c for c in text if c.isdigit() or c == '.')
            if clean_text:
                return int(float(clean_text))
            return 0
        except:
            return 0
    
    def extract_top_pages(self, email, password, categories, gender, min_followers, max_followers, max_pages=30, headless=False):
        """Extract top pages by engagement rate"""
        try:
            print("🚀 Starting advanced search for top pages")
            print("=" * 60)
            
            # Setup WebDriver
            if not self.setup_driver(headless):
                return None
            
            # Login to Sanjab
            if not self.login(email, password):
                return None
            
            # Navigate to advanced search
            if not self.navigate_to_advanced_search():
                return None
            
            # Apply filters
            if not self.apply_filters(categories, gender, min_followers, max_followers):
                return None
            
            # Execute search
            if not self.execute_search():
                return None
            
            # Extract results
            print("📊 Extracting page data...")
            results = []
            page_count = 0
            
            # Wait for results to load
            time.sleep(5)
            
            # Look for result elements
            result_elements = self.driver.find_elements(
                By.XPATH, 
                "//div[contains(@class, 'result') or contains(@class, 'item') or contains(@class, 'card')]"
            )
            
            if not result_elements:
                # Try alternative selectors
                result_elements = self.driver.find_elements(
                    By.XPATH, 
                    "//div[contains(@class, 'profile')] | //div[contains(@class, 'influencer')] | //div[contains(@class, 'page')]"
                )
            
            print(f"📋 Found {len(result_elements)} result elements")
            
            for element in result_elements:
                if page_count >= max_pages:
                    break
                
                try:
                    page_data = self.extract_page_data(element)
                    if page_data and page_data['page_name'] != "Unknown":
                        results.append(page_data)
                        page_count += 1
                        print(f"✅ Extracted page {page_count}: {page_data['page_name']}")
                    
                    # Small delay between extractions
                    time.sleep(0.5)
                    
                except Exception as e:
                    print(f"⚠️ Error extracting page {page_count + 1}: {str(e)}")
                    continue
            
            # Sort by engagement rate (descending)
            results.sort(key=lambda x: x['engagement_rate'], reverse=True)
            
            # Save to CSV
            if results:
                df = pd.DataFrame(results)
                output_filename = f'top_pages_engagement_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
                df.to_csv(output_filename, index=False, encoding='utf-8-sig')
                
                print(f"\n✅ Results saved to {output_filename}")
                print(f"📊 Total pages extracted: {len(results)}")
                print(f"🏆 Top 5 by engagement rate:")
                for i, page in enumerate(results[:5], 1):
                    print(f"   {i}. {page['page_name']} - {page['engagement_rate']}% engagement")
                
                return results
            else:
                print("❌ No pages found matching the criteria!")
                return None
                
        except Exception as e:
            print(f"❌ Error in advanced search: {str(e)}")
            return None
        finally:
            if self.driver:
                self.driver.quit()
                print("🔚 Browser closed")

if __name__ == "__main__":
    # Usage example
    searcher = SanjabAdvancedSearch()
    results = searcher.extract_top_pages(
        email="payegan@gmail.com",
        password="3xdVgd8XiMvxMPj",
        categories=["Family", "Lifestyle"],
        gender="Female",
        min_followers=50000,
        max_followers=500000,
        max_pages=30,
        headless=False
    )
