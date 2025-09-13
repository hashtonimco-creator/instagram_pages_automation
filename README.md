# Instagram Pages Automation Tool
## ابزار اتوماسیون تحلیل صفحات اینستاگرام

A comprehensive Instagram analytics automation tool designed for the Iranian market, specifically for analyzing lifestyle and women's style pages using the Sanjab platform.

---

## 🚀 Features

- **Sanjab Integration**: Automated login and data extraction from Sanjab platform
- **Lifestyle Analysis**: Specialized analysis for lifestyle and women's style Instagram pages
- **Engagement Metrics**: Comprehensive engagement rate analysis and ranking
- **CSV Reporting**: Detailed CSV reports with Persian language support
- **Influencer Search**: Advanced search functionality for finding relevant influencers
- **Web Automation**: Selenium-based automation for seamless data collection

---

## 📊 Analysis Results

### Top Lifestyle & Women's Style Pages (by Engagement Rate)

| Rank | Page | Engagement Rate | Category |
|------|------|----------------|----------|
| 1 | @parinaz_home20 | 10.96% | Lifestyle |
| 2 | @banoye_gilaniiiii | 10.86% | Lifestyle + Nature |
| 3 | @shadiibahrampoor | 10.67% | Lifestyle + Kids |
| 4 | @shabnam_shahrokhi | 10.41% | Lifestyle |
| 5 | @reyhaan_khanoomii | 10.01% | Lifestyle + Food |
| 6 | @negin_abedzadeh | 9.67% | Lifestyle |
| 7 | @alirezaajafarzadeh | 9.19% | Social + Lifestyle |
| 8 | @shervintarighaat | 9.13% | Lifestyle |
| 9 | @soogol_shakeri | 9.02% | Lifestyle |
| 10 | @iranian.beauty | 8.72% | Beauty |

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hashtonimco-creator/instagram_pages_automation.git
   cd instagram_pages_automation
   ```

2. **Set up virtual environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install ChromeDriver:**
   - Download ChromeDriver from [here](https://chromedriver.chromium.org/)
   - Add to system PATH or place in project directory

---

## 🎯 Usage

### 1. Influencer Search
```bash
python sanjab_influencer_search.py
```

### 2. Analytics Analysis
```bash
python sanjab_analytics.py
```

### 3. Complete Suite
```bash
python sanjab_complete_suite.py
```

### 4. Lifestyle Analysis
```bash
python create_lifestyle_analysis.py
```

---

## 📁 Project Structure

```
instagram_pages_automation/
├── sanjab_analytics.py          # Main analytics module
├── sanjab_influencer_search.py  # Influencer search functionality
├── sanjab_complete_suite.py     # Complete workflow automation
├── create_lifestyle_analysis.py # Lifestyle pages analysis
├── run_analytics_auto.py        # Automated analytics runner
├── lifestyle_pages.csv          # Lifestyle pages list
├── requirements.txt             # Python dependencies
├── .gitignore                   # Git ignore rules
└── README.md                    # This file
```

---

## 📈 Sample Output

The tool generates comprehensive CSV reports including:

- **Engagement Rate**: Percentage of followers who interact with content
- **Likes per Post**: Average likes per Instagram post
- **Comments per Post**: Average comments per post
- **Reel Views**: Average views for Instagram Reels
- **Shares**: Average shares per post
- **Follower Ratios**: Various engagement ratios

---

## 🔧 Configuration

### Sanjab Credentials
Update the credentials in the script files:
```python
EMAIL = "your_email@example.com"
PASSWORD = "your_password"
```

### Search Filters
Customize search parameters:
```python
category = "مد و فشن"  # Fashion & Style
follower_min = 1000    # Minimum followers
follower_max = 1000000 # Maximum followers
gender = "زن"          # Female
```

---

## 📊 Results Files

- `lifestyle_women_analysis_*.csv` - Detailed lifestyle pages analysis
- `comprehensive_instagram_analytics_*.csv` - Full analytics data
- `final_lifestyle_report.md` - Persian language report

---

## 🌟 Key Metrics Analyzed

1. **Engagement Rate**: Primary metric for page performance
2. **Likes per Post**: Content popularity indicator
3. **Comments per Post**: Audience interaction level
4. **Reel Performance**: Video content effectiveness
5. **Share Rate**: Content virality potential
6. **Follower Engagement**: Overall audience quality

---

## 📝 Notes

- Designed specifically for Iranian Instagram market
- Supports Persian/Farsi language content
- Optimized for lifestyle and beauty content analysis
- Compatible with Sanjab platform API
- Generates reports in both CSV and Markdown formats

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📄 License

This project is open source and available under the MIT License.

---

## 📞 Contact

- **GitHub**: [hashtonimco-creator](https://github.com/hashtonimco-creator)
- **Email**: hashtonim.co@gmail.com

---

*Built with ❤️ for the Iranian Instagram analytics community*