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

The scraping script is in `Book Scraping.py`.

---

🧼 Step 2: Data Cleaning

Tasks:
- Removed currency symbols (`£`)
- Extracted prices using list slicing
- Converted ratings from words (e.g. "Three") to numbers (e.g. 3)
- Checked for and handled missing values

Final cleaned data: `Cleaned Book Data.csv`

---

📊 Step 3: Exploratory Data Analysis

Questions I explored:
1. What’s the distribution of book prices?
![Distribution of book prices](https://github.com/user-attachments/assets/0df677f8-bcd3-4319-9e54-970d98145f1b)
2. What’s the count of books by rating?
   ![Book Count of ratings](https://github.com/user-attachments/assets/51c16ed7-c76d-40ab-b02f-e37043278022)

3. What are the average prices per category?
   ![Average book price per cateogry](https://github.com/user-attachments/assets/3f198d9c-dd4b-4cc4-9fd9-6b2e96e341e1)

4. Do higher-rated books tend to be more expensive?
   ![Book price by rating](https://github.com/user-attachments/assets/4f066272-f8c7-467a-ab00-da275a5adf34)





