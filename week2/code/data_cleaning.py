import pandas as pd
# Load the dataset
df = pd.read_csv("dirty_data_sample.csv")
# Check the original data
print("Original data:")
print(df)
df.info()
print(df.isnull().sum())
# Clean missing values
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Income"] = df["Income"].fillna(df["Income"].median())
df["Name"] = df["Name"].fillna("Unknown")
df["City"] = df["City"].fillna("Unknown")
# Remove duplicates
df = df.drop_duplicates()
print("\nCleaned data:")
print(df)
