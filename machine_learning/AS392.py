import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

#load the dataset
Datapath = "student_performance_ml.csv"
df = pd.read_csv(Datapath)

# Separate input features(X) and output (y)
X = df[['StudyHours','Attendance','PreviousScore','AssignmentsCompleted','SleepHours']]
y = df["FinalResult"]

#Split the dataset into the training an testing data
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

#Create decision tree model
model = DecisionTreeClassifier()

# train the model
model.fit(X_train,y_train)

print("Decision tree model trained successfully.")

#Predict the result for X_test
y_pred = model.predict(X_test)

#Display Actual and predicted Values
result = pd.DataFrame({"Actual": y_test,"Predicted":y_pred})

print(result)