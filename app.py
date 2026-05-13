import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(r"C:\Users\anamg\OneDrive\Desktop\HexSoftwares_Covid19_Project\covid.csv")

# Show first rows
print("\nFIRST 5 ROWS:\n")
print(df.head())

# Dataset info
print("\nDATASET INFO:\n")
print(df.info())

# Missing values
print("\nMISSING VALUES:\n")
print(df.isnull().sum())

# Top countries
country_cases = df.groupby("Country/Region")["Confirmed"].max()

top10 = country_cases.sort_values(ascending=False).head(10)

print("\nTOP 10 COUNTRIES:\n")
print(top10)

# Create graph
plt.figure(figsize=(12,6))

bars = plt.bar(top10.index, top10.values)

# Titles
plt.title("Top 10 Countries by Covid-19 Confirmed Cases")
plt.xlabel("Countries")
plt.ylabel("Confirmed Cases")

# Rotate names
plt.xticks(rotation=45)

# Add values on top
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval,
             int(yval),
             ha='center',
             va='bottom',
             fontsize=8)

plt.tight_layout()

plt.show()