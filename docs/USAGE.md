# 📖 Usage Guide
## Instagram Influencer Analysis Tool

## 🎯 Introduction

This tool is designed for analyzing and ranking Iranian Instagram influencers. Using this tool you can:

- Search for desired influencers
- Analyze page statistics and information
- Generate detailed reports
- Extract real data from Sanjab platform

## 🚀 Quick Start

### 1. Run the Tool
```bash
python main.py
```

### 2. Select Option from Menu
The tool provides a simple menu with the following options:

- **1. Search influencers from Sanjab**
- **2. Analyze existing pages**
- **3. Extract real data from Sanjab**
- **4. View previous results**
- **5. Usage guide**

## 🔍 Influencer Search

### Search Steps:
1. Select option 1 from menu
2. Email and password are automatically used (payegan@gmail.com)
3. Category is set to "Lifestyle" by default
4. Gender is set to "Female" by default

### Configurable Filters:
- **Category**: Lifestyle, Family, Cooking, Fashion, etc.
- **Gender**: Female or Male
- **Follower Range**: Configurable in code
- **Engagement Rate**: Minimum acceptable

## 📊 Page Analysis

### Analysis Steps:
1. Select option 2 from menu
2. Email and password are automatically used
3. Specify CSV file path (or press Enter to use latest file)

### Analyzed Information:
- Engagement rate (Engagement Rate)
- Follower count
- Average likes and comments
- Growth rate
- Audience quality

## 🔄 Real Data Extraction

### Prerequisites:
- Sanjab HTML file in `data/sanjab.html` folder

### Steps:
1. Select option 3 from menu
2. Tool automatically processes HTML file
3. Real data is extracted and saved in CSV

## 📋 View Results

### Available Reports:
- Markdown files in `results/` folder
- CSV files in `data/` folder

### Report Content:
- List of top pages
- Detailed statistics
- Advertising suggestions
- Performance categorization

## ⚙️ Advanced Settings

### Code Editing:
```python
# Set follower range
MIN_FOLLOWERS = 50000
MAX_FOLLOWERS = 500000

# Set number of pages to search
MAX_PAGES = 5

# Set browser mode
HEADLESS = False  # True to hide browser
```

### Filter Settings:
```python
# Allowed categories
ALLOWED_CATEGORIES = [
    "Lifestyle",
    "Family", 
    "Cooking",
    "Fashion"
]

# Allowed genders
ALLOWED_GENDERS = ["Female", "Male"]
```

## 🛠️ Troubleshooting

### Common Issues:

#### 1. ChromeDriver Error
```
❌ ChromeDriver not found
```
**Solution**: 
- Update Chrome
- Run `pip install --upgrade webdriver-manager`

#### 2. Sanjab Connection Error
```
❌ Error logging into Sanjab
```
**Solution**:
- Check internet connection
- Verify email and password
- Disable VPN

#### 3. CSV File Error
```
❌ CSV file not found
```
**Solution**:
- Check file path
- Place file in `data/` folder

## 📈 Practical Examples

### Example 1: Search Cooking Influencers
```python
searcher = SanjabInfluencerSearch()
searcher.run_influencer_search(
    email="payegan@gmail.com",
    password="3xdVgd8XiMvxMPj",
    category="Cooking",
    gender="Female",
    max_pages=3
)
```

### Example 2: Analyze Specific File
```python
analyzer = SanjabAnalytics()
analyzer.run_analysis(
    "data/my_pages.csv",
    "payegan@gmail.com",
    "3xdVgd8XiMvxMPj",
    headless=True
)
```

### Example 3: Extract Real Data
```python
from src.extract_sanjab_real_data import extract_sanjab_data
profiles = extract_sanjab_data()
```

## 🔒 Security Notes

### Information Protection:
- Never store email and password in code
- Use environment variables
- Add sensitive files to .gitignore

### Ethical Use:
- Use data legally
- Respect influencer privacy
- Follow Instagram rules

## 📞 Support

### Getting Help:
- **Documentation**: `docs/` folder
- **Examples**: Sample files in `data/`
- **Issues**: GitHub Issues

### Bug Reporting:
1. Describe the problem accurately
2. Provide complete error message
3. Write steps to reproduce the problem

---

**Note**: This guide is prepared for version 2.0.0 of the tool.