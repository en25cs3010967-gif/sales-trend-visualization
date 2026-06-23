import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/sales_data.csv")

# Convert date column
df['Date'] = pd.to_datetime(df['Date'])

# Create Month column
df['Month'] = df['Date'].dt.to_period('M')

# Monthly sales trend
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()

# Convert for plotting
monthly_sales['Month'] = monthly_sales['Month'].astype(str)

# 📈 Line Chart - Sales Trend
plt.figure(figsize=(10,5))
plt.plot(monthly_sales['Month'], monthly_sales['Sales'], marker='o')

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid()
plt.xticks(rotation=45)

plt.show()


# 📊 Product-wise Sales
product_sales = df.groupby('Product')['Sales'].sum()

plt.figure(figsize=(6,4))
plt.bar(product_sales.index, product_sales.values)

plt.title("Product-wise Sales")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.show()


#  Region-wise Sales
region_sales = df.groupby('Region')['Sales'].sum()

plt.figure(figsize=(6,6))
plt.pie(region_sales, labels=region_sales.index, autopct='%1.1f%%')

plt.title("Region-wise Sales Distribution")

plt.show()