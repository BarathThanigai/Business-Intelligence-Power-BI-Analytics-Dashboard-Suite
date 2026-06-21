# IMPORTING LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
print("Libraries imported successfully.")

# LOADING THE DATA
data = pd.read_csv('D:/Future_Interns/FUTURE_DS_01/Datasets/online_retail.csv')
print(data)
print("Data loaded successfully.")

# DATA DESCRIPTION
print("Data Shape:")
print(data.shape)

print("First 5 rows of the data:")
print(data.head())

print("Data Description:")
print(data.describe())

print("Data Information:")
print(data.info())

print("Missing Values:")
print(data.isna().sum())  # Checking for missing values in the dataset

print("Duplicate Values:")
print(data.duplicated().sum())  # Checking for duplicate values in the dataset

# DATA CLEANING AND TRANSFORMING
data['CustomerID'] = data['CustomerID'].fillna('Unknown')  # Handling missing customer IDs

data = data[data['UnitPrice'] > 0]  # Removing invalid unit prices

data['TransactionType'] = data['Quantity'].apply(  # Creating 'TransactionType' column to differentiate between sales and returns
    lambda x: 'Return' if x < 0 else 'Sale'
)

data['Revenue'] = data['Quantity'] * data['UnitPrice']  #Creating 'Revenue' column from 'Quantity' and 'UnitPrice'

# TOP PRODUCTS BY REVENUE
top_products = data.groupby('Description')['Revenue'].sum().sort_values(ascending=False).head(10)
print(top_products)

# COUNTRY-WISE REVENUE
country_sales = data.groupby('Country')['Revenue'].sum().sort_values(ascending=False)
print(country_sales.head(10))

# MONTHLY SALES TREND
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
data['MonthYear'] = data['InvoiceDate'].dt.to_period('M')
monthly_sales = data.groupby('MonthYear')['Revenue'].sum()
print(monthly_sales)

# MONTHLY TREND REVENUE VISUALIZATION
monthly_sales.plot(figsize=(12,6))
plt.title('Monthly Revenue Trend')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.show()

# TOP PRODUCTS CHART
top_products.plot(kind='bar', figsize=(12,6))
plt.title('Top Products by Revenue')
plt.xlabel('Product')
plt.ylabel('Revenue')
plt.show()

# COUNTRY-WISE REVENUE CHART
country_sales.head(10).plot(kind='bar', figsize=(12,6))
plt.title('Top 10 Countries by Revenue')
plt.xlabel('Country')
plt.ylabel('Revenue')
plt.show()