#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup script for Instagram Influencer Analysis Tool
"""

import os
import sys
import subprocess
import platform

def check_python_version():
    """Check Python version"""
    if sys.version_info < (3, 7):
        print("❌ Python 3.7 or higher is required!")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python {sys.version.split()[0]} - OK")
    return True

def create_directories():
    """Create required directories"""
    directories = ['src', 'data', 'results', 'docs', 'scripts']
    
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"📁 Directory {directory} created")
        else:
            print(f"✅ Directory {directory} exists")

def install_requirements():
    """Install dependencies"""
    try:
        print("📦 Installing dependencies...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def check_chrome():
    """Check for Chrome installation"""
    system = platform.system().lower()
    
    if system == "windows":
        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        ]
    elif system == "darwin":  # macOS
        chrome_paths = ["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"]
    else:  # Linux
        chrome_paths = ["/usr/bin/google-chrome", "/usr/bin/chromium-browser"]
    
    for path in chrome_paths:
        if os.path.exists(path):
            print("✅ Google Chrome found")
            return True
    
    print("⚠️  Google Chrome not found!")
    print("Please download and install Chrome from https://www.google.com/chrome/")
    return False

def create_sample_data():
    """Create sample file"""
    sample_content = """page_name,description,category
asalbano_life,Asal Bano/Lifestyle/Tips/Housekeeping,Lifestyle
life.nadi73,Nadia/Cooking/Lifestyle,Lifestyle
nazanintips,Nazanin Tips,Lifestyle"""
    
    sample_file = "data/sample_pages.csv"
    if not os.path.exists(sample_file):
        with open(sample_file, 'w', encoding='utf-8') as f:
            f.write(sample_content)
        print(f"📄 Sample file {sample_file} created")

def main():
    """Main setup function"""
    print("🚀 Setting up Instagram Influencer Analysis Tool")
    print("=" * 60)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Create directories
    print("\n📁 Creating project structure...")
    create_directories()
    
    # Install dependencies
    print("\n📦 Installing dependencies...")
    if not install_requirements():
        print("❌ Setup failed!")
        sys.exit(1)
    
    # Check Chrome
    print("\n🌐 Checking Chrome...")
    check_chrome()
    
    # Create sample files
    print("\n📄 Creating sample files...")
    create_sample_data()
    
    print("\n" + "=" * 60)
    print("✅ Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Prepare your Sanjab account")
    print("2. Place Sanjab HTML file in data folder")
    print("3. Run the tool with 'python main.py'")
    print("\n📖 For more guidance, read README.md")
    print("=" * 60)

if __name__ == "__main__":
    main()

