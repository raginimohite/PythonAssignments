import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
import matplotlib.pyplot as plt

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

#Calculate accuracy
accuracy = accuracy_score(y_test,y_pred)

#Display accuracy
print("Accuracy =",accuracy)

#Display accuracy in percentage
print("Accuracy = {:.2f}%".format(accuracy*100))

# Create confusion matrics
cm = confusion_matrix(y_test,y_pred)
# Display Confusion matrics
disp = ConfusionMatrixDisplay(confusion_matrix = cm)
   
disp.plot()

#show the graph
plt.show()

# Calculate Training Accuracy
train_accuracy = model.score(X_train, y_train)

# Calculate Testing Accuracy
test_accuracy = model.score(X_test, y_test)

# Display Training Accuracy
print("Training Accuracy =", train_accuracy)

# Display Testing Accuracy
print("Testing Accuracy =", test_accuracy)

# Compare both accuracies
if train_accuracy > test_accuracy:
    print("Model may be Overfitting.")
elif train_accuracy < test_accuracy:
    print("Model may be Underfitting.")
else:
    print("Model is performing well.")

# Model with max_depth = 1
model1 = DecisionTreeClassifier(max_depth=1, random_state=42)
model1.fit(X_train, y_train)
acc1 = model1.score(X_test, y_test)

# Model with max_depth = 3
model2 = DecisionTreeClassifier(max_depth=3, random_state=42)
model2.fit(X_train, y_train)
acc2 = model2.score(X_test, y_test)

# Model with max_depth = None
model3 = DecisionTreeClassifier(max_depth=None, random_state=42)
model3.fit(X_train, y_train)
acc3 = model3.score(X_test, y_test)

# Display Accuracies
print("\nTesting Accuracy for Different Models")
print("max_depth = 1 :", acc1)
print("max_depth = 3 :", acc2)
print("max_depth = None :", acc3)