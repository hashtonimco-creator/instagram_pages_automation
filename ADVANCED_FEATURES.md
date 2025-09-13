# ویژگی‌های پیشرفته Sanjab Analytics

## 🎯 جستجوی پیشرفته اینفلوئنسرها

### ویژگی‌های کلیدی

#### 1. جستجوی خودکار بر اساس فیلترها
- **دسته‌بندی**: انتخاب دسته‌بندی خاص (مد و فشن، ورزش، تکنولوژی، و غیره)
- **بازه فالوور**: تعیین حداقل و حداکثر تعداد فالوور
- **جنسیت**: فیلتر بر اساس جنسیت صاحب پیج (مرد، زن)
- **مرتب‌سازی**: مرتب‌سازی خودکار بر اساس نرخ تعامل (نزولی)

#### 2. استخراج هوشمند اینفلوئنسرها
- **XPath های متعدد**: استفاده از چندین روش برای یافتن اینفلوئنسرها
- **حذف تکرار**: جلوگیری از تکرار اینفلوئنسرها با استفاده از Set
- **بارگذاری خودکار**: بارگذاری نتایج از چندین صفحه
- **مدیریت خطا**: مدیریت خطاهای احتمالی در استخراج

#### 3. خروجی ساختاریافته
- **فایل CSV منظم**: ذخیره لیست اینفلوئنسرها در قالب CSV
- **اطلاعات تکمیلی**: شامل منبع و زمان کشف
- **پشتیبانی از فارسی**: encoding UTF-8-BOM برای Excel

## 🔄 مجموعه کامل ابزارها

### فرآیند یکپارچه

#### مرحله 1: جستجوی اینفلوئنسرها
```python
# تنظیم فیلترها
category = "مد و فشن"
follower_min = 10000
follower_max = 100000
gender = "زن"

# اجرای جستجو
searcher = SanjabInfluencerSearch()
searcher.run_influencer_search(email, password, category, follower_min, follower_max, gender)
```

#### مرحله 2: تحلیل آمار
```python
# تحلیل آمار اینفلوئنسرهای یافت شده
analyzer = SanjabAnalytics()
analyzer.run_analysis("influencers_search_results.csv", email, password)
```

#### مرحله 3: ترکیب نتایج
```python
# ترکیب نتایج جستجو و تحلیل
combined_df = pd.merge(search_df, analytics_df, on='page_name', how='left')
```

## 📊 فایل‌های خروجی

### 1. فایل جستجوی اینفلوئنسرها
```
influencers_search_results_YYYYMMDD_HHMMSS.csv
```

| ستون | توضیح |
|-------|-------|
| `page_name` | نام پیج اینستاگرام |
| `source` | منبع کشف (sanjab_search) |
| `discovered_at` | زمان کشف |

### 2. فایل تحلیل آمار
```
comprehensive_instagram_analytics_YYYYMMDD_HHMMSS.csv
```

| ستون | توضیح |
|-------|-------|
| `page_name` | نام پیج اینستاگرام |
| `engagement_rate` | نرخ تعامل |
| `engagement_rate_percentile` | رتبه نرخ تعامل |
| `better_than_percent` | درصد بهتر از سایر پیج‌ها |
| `similar_pages_percent` | درصد پیج‌های مشابه |
| `likes_per_post` | لایک به ازای هر پست |
| `comments_per_post` | کامنت به ازای هر پست |
| `views_to_follower_ratio` | نسبت بازدید به فالوور |
| `likes_to_follower_ratio` | نسبت لایک به فالوور |
| `average_reel_views` | میانگین بازدید Reel |
| `average_shares` | میانگین Share |
| `timestamp` | زمان تحلیل |

### 3. فایل ترکیبی
```
complete_analysis_YYYYMMDD_HHMMSS.csv
```

ترکیب کامل اطلاعات جستجو و تحلیل در یک فایل

## 🚀 نحوه استفاده

### اجرای جستجوی اینفلوئنسرها
```bash
# روش 1: اجرای ساده
python run_influencer_search.py

# روش 2: اجرای خودکار (Windows)
run_influencer_search.bat
```

### اجرای مجموعه کامل
```bash
# روش 1: اجرای کامل
python sanjab_complete_suite.py

# روش 2: اجرای خودکار (Windows)
run_complete_suite.bat
```

## ⚙️ تنظیمات پیشرفته

### فیلترهای جستجو
- **دسته‌بندی**: مد و فشن، ورزش، تکنولوژی، غذا، سفر، و غیره
- **بازه فالوور**: از 1,000 تا 10,000,000+
- **جنسیت**: مرد، زن، یا همه
- **مرتب‌سازی**: نرخ تعامل (نزولی)، تعداد فالوور، و غیره

### تنظیمات عملکرد
- **حداکثر صفحات**: تعداد صفحات برای بارگذاری (پیش‌فرض: 5)
- **حالت headless**: اجرای بدون نمایش مرورگر
- **تاخیر بین درخواست‌ها**: جلوگیری از محدودیت سرور

## 🔧 کلاس‌های اصلی

### SanjabInfluencerSearch
```python
class SanjabInfluencerSearch:
    def setup_driver(self, headless=False)
    def login_to_sanjab(self, email, password)
    def navigate_to_advanced_search(self)
    def set_search_filters(self, category, follower_min, follower_max, gender)
    def execute_search(self)
    def extract_influencers_from_results(self)
    def load_more_results(self, max_pages=5)
    def save_influencers_to_csv(self, filename=None)
    def run_influencer_search(self, ...)
```

### SanjabCompleteSuite
```python
class SanjabCompleteSuite:
    def get_credentials(self)
    def search_influencers(self)
    def analyze_influencers(self, csv_file=None)
    def combine_results(self)
    def run_complete_workflow(self)
```

## 📈 مزایای سیستم جدید

1. **خودکارسازی کامل**: از جستجو تا تحلیل و ترکیب نتایج
2. **فیلترهای پیشرفته**: جستجوی دقیق بر اساس معیارهای مختلف
3. **مدیریت فایل‌ها**: مدیریت خودکار فایل‌های ورودی و خروجی
4. **گزارش‌گیری جامع**: گزارش‌های کامل از تمام مراحل
5. **قابلیت توسعه**: ساختار ماژولار و قابل توسعه

---
*ویژگی‌های پیشرفته تکمیل شده در 13 سپتامبر 2025*
