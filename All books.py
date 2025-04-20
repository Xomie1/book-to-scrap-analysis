import requests
from bs4 import BeautifulSoup
import pandas as pd

#Define base url
base_site = "http://books.toscrape.com/"
home_url = base_site + "index.html"

#make request to homepage and parse with beautifulsoup
response = requests.get(home_url)
soup = BeautifulSoup(response.text, 'html.parser')

#find all categories in the sidebar
category_section = soup.find("div", class_="side_categories")
category_links = category_section.find_all("a")[1:] #skip the first "books" link

#prepare a list to collect al the book
all_book = []

#loop through each category
for category in category_links:
    category_name =  category.text.strip() #clean the category name
    category_href = category["href"].replace("../","") #clean the link
    category_url = base_site + category_href #full url to the category

    print(f" Scraping category: {category_name}")
    next_page_url = category_url #start with first page of the category

    #scrape all pages in the current category
    while next_page_url:
        response = requests.get(next_page_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        #find all books
        books = soup.find_all("article", class_="product_pod")

        #loop through each book and extract details
        for book in books:
            title = book.h3.a["title"]
            price = book.find("p",class_="price_color").text
            rating = book.p["class"][1] #rating as a word

            all_book.append({
                "Title": title,
                "Price": price,
                "Rating": rating,
                "Category": category_name
            })

        #check if there is a "next" button
        next_btn = soup.find("li", attrs={"class": "next"})
        if next_btn:
            next_page_relative = next_btn.a["href"]
            #handle pagination by updating next page url
            next_page_url = category_url.replace("index.html", "") + next_page_relative
        else:
            next_page_url = None #no more pages

#convert books to csv
df = pd.DataFrame(all_book)
df.to_csv("Book Data.csv", index=False)

print("Completed!!!")