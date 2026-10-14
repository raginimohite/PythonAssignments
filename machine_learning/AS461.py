import pandas as pd
#step 3
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#--------------Step 1:--------------

#Load the data
Datapath = "MarvellousAdvertising.csv" 
df = pd.read_csv(Datapath,sep="\t")

print(df)

#-------------Step 2 :----------------

# Clean Prepare and manipulate
print(df.head())

#Check the missing values
print("\n")
print(df.isnull().sum())

#Create input features
X = df[['TV','radio','newspaper']]

#Create output features
Y = df['sales']

#Display input and output
print("\nInput features:")
print(X)

print("\nOutut features:")
print(Y)

#--------------Step 3-------------------

#Split the data into 50% training and 50% testing
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.5,random_state=42)

#Create linear model
model= LinearRegression()

#train the model
model.fit(X_train,Y_train)

print("\nModel training completed successfully:")

#-----------------Step 4-------------------------

# Test the model using testing data
Y_pred = model.predict(X_test)

print("\nPredicted sales:")
print(Y_pred)

#--------------------Step 5------------------

# Cmpare actual and predicted sales
Comparison = pd.DataFrame({"Expected sales":Y_test.values,"Predicted sales":Y_pred})

print("\n")
print(Comparison)
