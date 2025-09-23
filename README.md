# 🎯 Instagram Influencer Analysis Tool

A powerful tool for extracting, analyzing and ranking Iranian Instagram influencers in various domains, especially lifestyle and family.

## ✨ Features

- 🔍 **Advanced Search**: Search influencers with various filters
- 📊 **Comprehensive Analysis**: Calculate engagement rate, follower stats and key metrics
- 🎯 **Smart Categorization**: Filter by topic, gender and follower count
- 📈 **Reporting**: Generate detailed and understandable reports
- 🔄 **Data Extraction**: Extract real information from Sanjab platform
- 📁 **Organization**: Clean and professional project structure

## 🏗️ Project Structure

```
sanjab_analysis/
├── src/                          # Main code files
│   ├── sanjab_analytics.py      # Page analysis class
│   ├── sanjab_influencer_search.py  # Influencer search class
│   ├── sanjab_complete_suite.py # Complete suite class
│   └── extract_sanjab_real_data.py  # Real data extraction
├── data/                         # Data files
│   ├── sanjab.html              # Sanjab HTML file
│   ├── sanjab_files/            # Related Sanjab files
│   └── *.csv                    # CSV data files
├── results/                      # Generated reports
│   └── *.md                    # Detailed reports
├── docs/                        # Documentation
├── scripts/                     # Helper scripts
├── main.py                      # Main execution file
├── requirements.txt             # Dependencies
└── README.md                    # This file
```

## 🚀 Installation and Setup

### Prerequisites
- Python 3.7 or higher
- Valid Sanjab account
- Chrome browser

### Installation Steps

1. **Clone the project**:
```bash
git clone https://github.com/hashtonimco-creator/instagram_pages_automation.git
cd instagram_pages_automation
```

2. **Create virtual environment**:
```bash
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Run the tool**:
```bash
python main.py
```

## 🎮 Usage

### Method 1: Text Interface
```bash
python main.py
```
Then select the desired option from the displayed menu.

### Method 2: Direct Execution
```python
from src.sanjab_analytics import SanjabAnalytics
from src.sanjab_influencer_search import SanjabInfluencerSearch

# Search influencers
searcher = SanjabInfluencerSearch()
searcher.run_influencer_search(
    email="payegan@gmail.com",
    password="3xdVgd8XiMvxMPj",
    category="Lifestyle",
    gender="Female"
)

# Analyze pages
analyzer = SanjabAnalytics()
analyzer.run_analysis("data/pages.csv", "email", "password")
```

## 📊 Sample Results

### Top 10 Lifestyle and Family Pages:

| Rank | Page Name | Engagement Rate | Followers | Description |
|------|-----------|-----------------|-----------|-------------|
| 1 | **@asalbano_life** | 87.28% | 153,498 | Asal Bano/Daily Life/Tips/Housekeeping |
| 2 | **@life.nadi73** | 44.14% | 68,976 | Nadia/Cooking/Lifestyle |
| 3 | **@nazanintips** | 24.91% | 187,639 | Nazanin Tips ✨ |
| 4 | **@shiriino__** | 24.65% | 260,575 | Shirin |
| 5 | **@shaqayeqnoie** | 23.76% | 167,154 | Shaghayegh Noei |

## 🔧 Advanced Settings

### Search Filter Settings:
```python
# Follower range
min_followers = 50000
max_followers = 500000

# Categories
categories = ["Lifestyle", "Family", "Cooking"]

# Gender
gender = "Female"  # or "Male"
```

### Browser Settings:
```python
# Headless mode
headless = True

# Chrome options
chrome_options = [
    "--no-sandbox",
    "--disable-dev-shm-usage",
    "--disable-gpu"
]
```

## 📈 Analysis Metrics

- **Engagement Rate**: Percentage of audience engagement
- **Follower Count**: Number of followers
- **Average Likes**: Average likes per post
- **Average Comments**: Average comments per post
- **Growth Rate**: Follower growth speed
- **Audience Quality**: Percentage of real followers

## 🛠️ Troubleshooting

### Common Issues:

1. **ChromeDriver Error**:
```bash
pip install --upgrade webdriver-manager
```

2. **Selenium Error**:
```bash
pip install --upgrade selenium
```

3. **Sanjab Connection Issue**:
- Check internet connection
- Verify email and password
- Disable VPN

## 📝 License and Contribution

This project is released under MIT license. To contribute:

1. Fork the project
2. Create a new branch
3. Commit your changes
4. Send a Pull Request

## 📞 Support

- **Email**: hashtonim.co@gmail.com
- **GitHub Issues**: [Issues Page](https://github.com/hashtonimco-creator/instagram_pages_automation/issues)
- **Documentation**: `docs/` folder

## 🎯 Commercial Use

This tool is designed for commercial and marketing purposes. In commercial use:

- Follow Instagram rules
- Respect influencer privacy
- Use data ethically

---

**Developer**: Hashtonim Creator  
**Version**: 2.0.0  
**Last Updated**: September 14, 2025