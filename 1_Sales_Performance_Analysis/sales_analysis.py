import pandas as pd
import matplotlib.pyplot as plt
import os

# Get script location
base_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_path, "sales_data.csv")

# Load dataset
df = pd.read_csv(file_path)

print("\nDataset Loaded Successfully\n")
print(df.head())

# Convert column names to lowercase
df.columns = df.columns.str.lower()

# Convert sales column to numeric (VERY IMPORTANT FIX)
df["sales"] = pd.to_numeric(df["sales"], errors="coerce")

# Remove rows where sales is NaN (if any)
df = df.dropna(subset=["sales"])

# Total Sales
total_sales = df["sales"].sum()
print("\nTotal Sales:", total_sales)

# Average Sales
avg_sales = df["sales"].mean()
print("Average Sales:", avg_sales)

# Sales by Region
region_sales = df.groupby("region")["sales"].sum()
print("\nSales by Region:\n", region_sales)

# Plot
plt.figure()
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()
