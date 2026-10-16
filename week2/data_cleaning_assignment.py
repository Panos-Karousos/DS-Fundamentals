 #Import pandas
import pandas as pd

# Load the CSV and preview its contents
df = pd.read_csv("dirty_data_sample.csv")
df

#find duplicated rows
df.duplicated()

#Statistical Summary generation.
df.describe(include="all")


#Number of missing values.
df.isnull().sum()

#Check Data Types.
df.dtypes

#Convert age to numerical:
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
df.dtypes


#Fill the missing values with the median:
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Income"] = df["Income"].fillna(df["Income"].median())

#Fill the missing values with Uknown:
df["Name"] = df["Name"].fillna("Unknown")
df["City"] = df["City"].fillna("Unknown")
df = df.drop_duplicates()



df

#Check that there are no missing values and no duplicated rows:
df.isnull().sum()
df.dtypes
df.duplicated().sum()



df.info()
df.describe(include="all")
