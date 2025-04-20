📘 Analyzing Book Prices and Ratings from Books to Scrape

This project explores and visualizes book data scraped from [Books to Scrape](http://books.toscrape.com), a free website for practicing web scraping. It's my first full data analysis project involving web scraping, cleaning, and exploratory data analysis (EDA).

---

🛠️ Tools Used
- Python 🐍
- requests
- BeautifulSoup
- pandas
- matplotlib & seaborn
- Excel (for quick chart validation)

---

🕸️ Step 1: Web Scraping

I scraped the following fields:
- Title
- Price
- Rating
- Category

The scraping script is in `/scripts/scrape_books.py`.

---

🧼 Step 2: Data Cleaning

Tasks:
- Removed currency symbols (`£`)
- Extracted prices using list slicing
- Converted ratings from words (e.g. "Three") to numbers (e.g. 3)
- Checked for and handled missing values

Final cleaned data: `/data/all_books_clean.csv`

---

📊 Step 3: Exploratory Data Analysis

Questions I explored:
1. What’s the distribution of book prices?
2. What’s the count of books by rating?
3. What are the average prices per category?
4. Do higher-rated books tend to be more expensive?




