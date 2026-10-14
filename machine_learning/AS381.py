import pandas as pd

Border = "-"*30

########################################
# Step 1 : Load the dataset
########################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

Datapath = "student_performance_ml.csv"
df = pd.read_csv(Datapath)

print("Dataset loaded succesfully")
print("first five records")
print(df.head())

print("Dataset loaded succesfully")
print("last five records")
print(df.tail())

print(Border)
print("Step 2 : Data analysis")
print(Border)

print("shape of database:",df.shape)

print("list of clumn names:",list(df.columns))

print("datatypes of each columns:")
print(df.describe())



