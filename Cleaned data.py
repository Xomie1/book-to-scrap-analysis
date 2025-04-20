import pandas as pd

df = pd.read_csv("Book Data.csv")

#clean the prices column
prices = [item[item.index("£")+1:] for item in df["Price"]]
df["Price"] = prices

#clean the rating column
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
} 
df["Rating"] = df["Rating"].map(rating_map)

#check for missing values
print("Missing values:\n", df.isnull().sum())

#save cleaned data
df.to_csv("Cleaned Book Data.csv", index=False)
print("Cleaned!!!")