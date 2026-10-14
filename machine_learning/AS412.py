import pandas as pd
from sklearn.model_selection import train_test_split

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

#Check missing values
print("\n Missing values:")
print(df.isnull().sum())

#Separate features X and target Y
X = df.drop("Class",axis=1)
y = df["Class"]

print("\n Features (X):")
print(X.head())

print("\n Target (y):")
print(y.head())

#split the data into training and testing data
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

print("\n Training data shape :")
print(X_train.shape)

print("\n Testing data shape :")
print(X_test.shape)

