import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt 
from sklearn.metrics import ConfusionMatrixDisplay

df = pd.read_csv("Employee_Attrition.csv")

#--------Step 2 --------------
print(df.shape)
print(df.columns)
print(df.head())

#--------Step 3--------------
print(df.isnull().sum())

#--------Step 5--------------
df["OverTime"] = df["OverTime"].map({"Yes":1,"No":0})

#--------Step 6--------------
df["Attrition"] = df["Attrition"].map({"Yes":1,"No":0})

#---------Step 7-------------------
X = df.drop("Attrition",axis=1)
Y = df["Attrition"]

#---------Step 8-------------------

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

#----------step 9:aplly appreciate fetaure scaling-----------

scalar = StandardScaler()
X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

#---------------step 10-------------------

model = MLPClassifier(
    hidden_layer_sizes=(64,32),
    activation="relu",
    solver="adam",
    max_iter= 500,
    random_state=42
)

#------------step 11 :model train-----------------

model = model.fit(X_train,Y_train)

#-----------step 12 : display iteration---------------

print("Iteration:",model.n_iter_)

#----------Step 13 : training Accuracy

train_accuracy = model.score(X_train,Y_train)
print("Training Accuracy:",train_accuracy)

#----------step 14 : ------------------

test_accuracy = model.score(X_test,Y_test)
print("Testing Accuracy :",test_accuracy)

#-----------Step 15 ---------------------

Y_pred = model.predict(X_test)
cm = confusion_matrix(Y_test,Y_pred)
print(cm)

#-------------step 16 :-------------------

ConfusionMatrixDisplay.from_predictions(Y_test,Y_pred)

plt.title("Employee Attrition Confusion Matrix")
plt.show()

#-----------------Step 17----------------------

plt.plot(model.loss_curve_)
plt.title("MLP training loss Curve")
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.show()

def PredictAttrition(employee_data):
    employee_df = pd.DataFrame([employee_data])
    employee_df["OverTime"]=employee_df["OverTime"].map({
        "Yes":1,
        "No":0
    })

    employee_scaled =scalar.transform(employee_df)
    prediction = model.predict(employee_scaled)

    if prediction[0] == 1:
        return "Employee is likely to leave"
    else:
        return "Employee is likely to stay"


new_employee = {
    "Age": 30,
    "MonthlyIncome": 4000,
    "YearsAtCompany": 3,
    "TotalWorkingYears": 7,
    "DistanceFromHome": 15,
    "JobSatisfaction": 2,
    "WorkLifeBalance": 2,
    "OverTime": "Yes",
    "NumCompaniesWorked": 3,
    "TrainingTimesLastYear": 2
}

print(PredictAttrition(new_employee))

employees = [
    {
        "Age": 25,
        "MonthlyIncome": 3000,
        "YearsAtCompany": 2,
        "TotalWorkingYears": 5,
        "DistanceFromHome": 10,
        "JobSatisfaction": 2,
        "WorkLifeBalance": 2,
        "OverTime": "Yes",
        "NumCompaniesWorked": 3,
        "TrainingTimesLastYear": 2
    },

    # Employee 2
    # Employee 3
    # Employee 4
    # Employee 5
]

for emp in employees:
    print(PredictAttrition(emp))

employes = [
    {
        "Age": 26,
        "MonthlyIncome": 42000,
        "YearsAtCompany": 3,
        "TotalWorkingYears": 5,
        "DistanceFromHome": 10,
        "JobSatisfaction": 2,
        "WorkLifeBalance": 2,
        "OverTime": "Yes",
        "NumCompaniesWorked": 3,
        "TrainingTimesLastYear": 2
    },

    # Employee 2
    # Employee 3
    # Employee 4
    # Employee 5
]

for emp in employes:
    print(PredictAttrition(emp))

employyes = [
    {
        "Age": 27,
        "MonthlyIncome": 195000,
        "YearsAtCompany": 13,
        "TotalWorkingYears": 14,
        "DistanceFromHome": 2,
        "JobSatisfaction": 2,
        "WorkLifeBalance": 2,
        "OverTime": "No",
        "NumCompaniesWorked": 3,
        "TrainingTimesLastYear": 2
    },

    # Employee 2
    # Employee 3
    # Employee 4
    # Employee 5
]

for emp in employyes:
    print(PredictAttrition(emp))


