import pandas as pd
#step 2
from sklearn.preprocessing import LabelEncoder
#step 3
from sklearn.neighbors import KNeighborsClassifier
#Step 5
from sklearn.metrics import accuracy_score

# Step 1: Get data
Datapath = "MarvellousInfosystem_PlayPredictor.csv"
df = pd.read_csv(Datapath,sep="\t")
print(df)

# Step 2 : Clean prepare and manipulate data
le = LabelEncoder()

df["Wether"] = le.fit_transform(df["Wether"])
df["Temperature"] = le.fit_transform(df["Temperature"])
df["Play"] = le.fit_transform(df["Play"])

print("\nEncoded Data:")
print(df)

# Step 3 : Train the data

#Features
X = df[["Wether","Temperature"]]

#Target
Y = df["Play"]

#create KNN model
model = KNeighborsClassifier(n_neighbors=3)

#Train the model
model.fit(X,Y)

print("\nModel Training Completed")

#Step 4: Test data
test_data = [[1,2]]

prediction = model.predict(test_data)

if prediction[0] == 1:
    print("prediction: Yes")
else:
    print("prediction : No")

#Step 5: Calculate Accuracy

#Predict the output for the data
Y_pred = model.predict(X)

#Calculate accuracy
accuracy = accuracy_score(Y,Y_pred)

print("\nAccuracy:",accuracy * 100,"%")

