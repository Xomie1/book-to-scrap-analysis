import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
#Load cleaned data
df = pd.read_csv("Cleaned Book Data.csv")

#1. What’s the distribution of book prices?
plt.figure(figsize=(10,5))
sns.histplot(df["Price"], bins=30, kde=True, color="skyblue")
plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.show()

#2. What's the count of books by rating?
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Rating", palette="viridis")
plt.title("Book Count by Ratings")
plt.xlabel("Ratings")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.show()

#3. What are the average prices per category?
avg_price_per_category = df.groupby("Category")["Price"].mean().sort_values()

plt.figure(figsize=(10,4))
avg_price_per_category.plot(kind="barh", color="blue")
plt.title("Average Book Price per Category")
plt.xlabel("Average Price (£)")
plt.ylabel("Category")
plt.tight_layout()
plt.show()

#4. Do higher-rated books tend to be more expensive?
plt.figure(figsize=(10,5))
sns.boxplot(data=df, x="Rating", y="Price", palette="coolwarm")
plt.title("Book Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Price (£)")
plt.tight_layout()
plt.show()


