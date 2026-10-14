import pandas as pd

# step 1: get data
DataPath = "WinePredicter.csv"

df = pd.read_csv(DataPath,sep="\t")

print("First 5 records:")
print(df.head())

print("\n Dataset shape:")
print(df.shape)

print("\n Column name")
print(df.columns)

# Step 2 : Clean,Prepare and manipulate Data

