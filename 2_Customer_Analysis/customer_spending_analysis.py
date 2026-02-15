
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Mall_Customers.csv")

# Display first rows
print(df.head())

# Basic info
print(df.info())

# Rename columns (if needed)
df.columns = df.columns.str.replace(' ', '_')

# Create spending categories
def spending_category(score):
    if score >= 70:
        return "High"
    elif score >= 40:
        return "Medium"
    else:
        return "Low"

df["Spender_Category"] = df["Spending_Score_(1-100)"].apply(spending_category)

# Count of each category
print(df["Spender_Category"].value_counts())

# Average income per category
print(df.groupby("Spender_Category")["Annual_Income_(k$)"].mean())

# Average age per category
print(df.groupby("Spender_Category")["Age"].mean())

# -----------------------------------
# VISUALIZATIONS
# -----------------------------------

# 1. Count plot
plt.figure(figsize=(6,4))
sns.countplot(x="Spender_Category", data=df)
plt.title("Customer Spending Category Distribution")
plt.show()

# 2. Income vs Spending Score
plt.figure(figsize=(7,5))
sns.scatterplot(
    x="Annual_Income_(k$)",
    y="Spending_Score_(1-100)",
    hue="Spender_Category",
    data=df
)
plt.title("Income vs Spending Score")
plt.show()

# 3. Age Distribution by Category
plt.figure(figsize=(7,5))
sns.boxplot(
    x="Spender_Category",
    y="Age",
    data=df
)
plt.title("Age Distribution by Spending Category")
plt.show()

print("Analysis Completed Successfully!")