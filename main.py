#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Instagram Influencer Analysis Tool

This tool is designed for extracting and analyzing Iranian Instagram pages
in the lifestyle and family domains.
"""

import sys
import os
from datetime import datetime

# Add src folder to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

def show_menu():
    """Display main menu"""
    print("=" * 60)
    print("🎯 Instagram Influencer Analysis Tool")
    print("=" * 60)
    print("1. Search influencers from Sanjab")
    print("2. Analyze existing pages")
    print("3. Extract real data from Sanjab")
    print("4. Extract top 30 pages by engagement rate")
    print("5. View previous results")
    print("6. Usage guide")
    print("0. Exit")
    print("=" * 60)

def run_influencer_search():
    """Execute influencer search"""
    try:
        from sanjab_influencer_search import SanjabInfluencerSearch
        
        print("🔍 Searching influencers from Sanjab")
        print("-" * 40)
        
        # Use default credentials automatically
        email = "payegan@gmail.com"
        password = "3xdVgd8XiMvxMPj"
        category = "Lifestyle"
        gender = "Female"
        
        print(f"Using email: {email}")
        print(f"Using category: {category}")
        print(f"Using gender: {gender}")
        
        # Execute search
        searcher = SanjabInfluencerSearch()
        searcher.run_influencer_search(
            email=email,
            password=password,
            category=category,
            gender=gender,
            max_pages=5,
            headless=False
        )
        
        print("✅ Search completed successfully!")
        
    except ImportError:
        print("❌ Error: sanjab_influencer_search.py file not found!")
    except Exception as e:
        print(f"❌ Error in search: {str(e)}")

def run_analytics():
    """Execute page analysis"""
    try:
        from sanjab_analytics import SanjabAnalytics
        
        print("📊 Analyzing Instagram pages")
        print("-" * 40)
        
        # Use default credentials automatically
        email = "payegan@gmail.com"
        password = "3xdVgd8XiMvxMPj"
        
        print(f"Using email: {email}")
        
        # Find the latest CSV file
        csv_file = None
        data_dir = "data"
        if os.path.exists(data_dir):
            csv_files = [f for f in os.listdir(data_dir) if f.endswith('.csv')]
            if csv_files:
                csv_file = os.path.join(data_dir, csv_files[0])
                print(f"Using file: {csv_file}")
        
        if not csv_file or not os.path.exists(csv_file):
            print(f"❌ No CSV file found in {data_dir}!")
            return
        
        # Execute analysis
        analyzer = SanjabAnalytics()
        analyzer.run_analysis(csv_file, email, password, headless=False)
        
        print("✅ Analysis completed successfully!")
        
    except ImportError:
        print("❌ Error: sanjab_analytics.py file not found!")
    except Exception as e:
        print(f"❌ Error in analysis: {str(e)}")

def extract_real_data():
    """Extract real data from Sanjab"""
    try:
        from extract_sanjab_real_data import extract_sanjab_data
        
        print("🔄 Extracting real data from Sanjab")
        print("-" * 40)
        
        # Check for HTML file
        html_file = "data/sanjab.html"
        if not os.path.exists(html_file):
            print(f"❌ File {html_file} not found!")
            print("Please place the Sanjab HTML file in the data folder first.")
            return
        
        # Execute extraction
        profiles = extract_sanjab_data()
        
        if profiles:
            print(f"✅ {len(profiles)} real pages extracted!")
        else:
            print("❌ No real pages found!")
        
    except ImportError:
        print("❌ Error: extract_sanjab_real_data.py file not found!")
    except Exception as e:
        print(f"❌ Error in extraction: {str(e)}")

def extract_top_30_pages():
    """Extract top 30 pages by engagement rate from Sanjab advanced search"""
    try:
        from sanjab_advanced_search import SanjabAdvancedSearch
        
        print("🏆 Extracting top 30 pages by engagement rate")
        print("-" * 50)
        
        # Use default credentials automatically
        email = "payegan@gmail.com"
        password = "3xdVgd8XiMvxMPj"
        
        print(f"Using email: {email}")
        print("Searching for pages with:")
        print("- Categories: Family, Lifestyle")
        print("- Gender: Female")
        print("- Follower range: 50,000 - 500,000")
        print("- Target: Top 30 by engagement rate")
        
        # Execute advanced search
        searcher = SanjabAdvancedSearch()
        results = searcher.extract_top_pages(
            email=email,
            password=password,
            categories=["Family", "Lifestyle"],
            gender="Female",
            min_followers=50000,
            max_followers=500000,
            max_pages=30,
            headless=False
        )
        
        if results:
            print(f"✅ Successfully extracted {len(results)} top pages!")
            print("Results saved to CSV file.")
        else:
            print("❌ No pages found matching the criteria!")
        
    except ImportError:
        print("❌ Error: sanjab_advanced_search.py file not found!")
    except Exception as e:
        print(f"❌ Error in extraction: {str(e)}")

def show_results():
    """Display previous results"""
    print("📋 Previous Results")
    print("-" * 40)
    
    # Check result files
    results_dir = "results"
    if os.path.exists(results_dir):
        result_files = [f for f in os.listdir(results_dir) if f.endswith('.md')]
        if result_files:
            print("Available report files:")
            for i, file in enumerate(result_files, 1):
                print(f"{i}. {file}")
            
            try:
                choice = int(input("File number to view (0 to go back): "))
                if 1 <= choice <= len(result_files):
                    file_path = os.path.join(results_dir, result_files[choice-1])
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        print("\n" + "="*60)
                        print(content[:1000] + "..." if len(content) > 1000 else content)
                        print("="*60)
            except (ValueError, IndexError):
                print("❌ Invalid selection!")
        else:
            print("No report files found!")
    else:
        print("Results folder not found!")

def show_help():
    """Display help guide"""
    help_text = """
📖 Instagram Influencer Analysis Tool Usage Guide

🔍 Influencer Search:
   - Uses Sanjab account to search for desired influencers
   - Results are saved in CSV file

📊 Page Analysis:
   - Analyzes pages from existing CSV file
   - Provides detailed statistics including engagement rate, followers, etc.

🔄 Real Data Extraction:
   - Extracts real page data from Sanjab HTML file
   - No internet connection required

🏆 Top 30 Pages by Engagement Rate:
   - Advanced search on Sanjab platform
   - Filters: Family & Lifestyle categories, Female gender
   - Follower range: 50,000 - 500,000
   - Extracts top 30 pages sorted by engagement rate
   - Results saved to CSV file

📋 View Results:
   - Displays previous reports

📁 Project Structure:
   - src/: Main code files
   - data/: Data files
   - results/: Generated reports
   - docs/: Documentation

🔧 Prerequisites:
   - Python 3.7+
   - Required libraries (selenium, pandas, numpy)

📞 Support:
   - For technical issues, check requirements.txt file
   - Use valid Sanjab account
"""
    print(help_text)

def main():
    """Main function"""
    while True:
        show_menu()
        
        try:
            choice = input("Your choice (0-6): ").strip()
            
            if choice == "0":
                print("👋 Goodbye!")
                break
            elif choice == "1":
                run_influencer_search()
            elif choice == "2":
                run_analytics()
            elif choice == "3":
                extract_real_data()
            elif choice == "4":
                extract_top_30_pages()
            elif choice == "5":
                show_results()
            elif choice == "6":
                show_help()
            else:
                print("❌ Invalid choice! Please enter a number 0-6.")
            
            input("\n⏸️  Press Enter to continue...")
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()

