import requests
from bs4 import BeautifulSoup
import pandas as pd

book_data = []

for page in range(1, 20):
    url = f"https://book.toscrape.com/catalogue/page-{page}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = soup.find_all('article', class_="product_pod")

    for book in books:
        title = book.h3.a["title"]
        price = book.find("p", class_="price_color").text
        rating = book.p["class"][1]
        

        book_data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
        })

#Save to CSV
df = pd.DataFrame(book_data)
df.to_csv("books.csv", index=False)