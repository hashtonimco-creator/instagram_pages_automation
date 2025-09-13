@echo off
echo Initializing Git repository and pushing to GitHub...

echo Setting up Git configuration...
git config --global user.name "hashtonimco-creator"
git config --global user.email "hashtonim.co@gmail.com"

echo Adding all files...
git add .

echo Committing files...
git commit -m "Add Instagram Pages Automation Tool - Complete Sanjab Analytics Suite

Features:
- Sanjab Instagram analytics automation
- Lifestyle and women's style pages analysis
- Selenium-based web automation
- Comprehensive CSV reporting
- Persian/Farsi language support
- Influencer search and engagement analysis"

echo Setting main branch...
git branch -M main

echo Pushing to GitHub...
git push -u origin main

echo Done! Check your repository at: https://github.com/hashtonimco-creator/instagram_pages_automation
pause
