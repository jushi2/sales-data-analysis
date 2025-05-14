#Importing pandas file and read that file

import pandas as pd
import numpy as np
df = pd.read_csv("sales_data.csv")

#drop rows with missing product or category
df = df.dropna(subset=["Product", "Category"])
#Converting panda to numpy
np_array = df.to_numpy()
print("Converting panda to numpy array:\n")
print(np_array)

data = np.loadtxt("sales_data.csv", delimiter=",",usecols=[3,4],skiprows=1)
#print(data)
#fill missing price with mean data
df["Price"] = df["Price"].fillna(df["Price"].mean())

#Fill missing Quantity with 0
df["Quantity"] = df["Quantity"].fillna(0)

#Analysis the Data

#Total revenue
df["Revenue"] = df["Price"] * df["Quantity"]

#Total Revenue by Per product
print("Total Revenue by per product:\n")
print(df.groupby("Product")["Revenue"].sum())

#total revenue by per category
print("Total revenue by per category:\n")
print(df.groupby("Category")["Revenue"].sum())

#Products with above-average prices
average_price = df["Price"].mean()
above_average = df["Price"][df["Price"] > average_price]
print("Products with above-average prices:\n")
print(df[df["Price"] > average_price][["Product", "Price"]])


#Top 3 performing products
product_performance = df.groupby("Product")["Quantity"].sum()
sorted_performance = product_performance.sort_values(ascending=False)
print("Top 3 performing products:\n")
print(sorted_performance[:3])

#Region wise best sell
region_sales = df.groupby("Region")["Revenue"].sum()

#Best region and worst selling
best_region = region_sales.idxmax()
worst_region = region_sales.idxmin()
print("Best Region:",best_region)
print("Worst Region:",worst_region)

df.groupby("Product")["Revenue"].sum().to_csv("product_revenue.csv")

import matplotlib.pyplot as plt

# Bar chart of revenue by category
df.groupby("Category")["Revenue"].sum().plot(kind="bar", title="Revenue by Category", ylabel="Revenue", xlabel="Category", colormap='viridis')
plt.grid(True)
plt.tight_layout()
plt.show()