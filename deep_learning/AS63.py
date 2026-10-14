import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
from sklearn.metrics import(precision_score,recall_score,f1_score)

df = pd.read_csv("Loan_Default.csv")
print(df.head())

#------------Step 3---------------
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df.head())

#-------------Step 4------------------

print(df.isnull().sum())

df["Income"] = df["Income"].fillna(df["Income"].median())

df["HomeOwnership"] = df["HomeOwnership"].fillna(df["HomeOwnership"].mode()[0])

#-------------Step 5-------------------

print(df["Default"].value_counts())

print(df["Default"].value_counts(normalize=True)*100)

#--------------step 6-------------------

df["PreviousDefault"] = df["PreviousDefault"].map({"Yes":1,"No":0})

df = pd.get_dummies(
    df,
    columns=["HomeOwnership"],
    drop_first=True
)

#-------------Step 7 ---------------------

X = df.drop("Default",axis=1)
Y = df["Default"]

#--------------Step 8 --------------------

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

#---------------Step 10----------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ------------------Step 11:-----------------

model = MLPClassifier(
    hidden_layer_sizes=(32,16),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)

#------------Step 12--------------------------

model.fit(X_train,Y_train)

#-------------step 13-----------------------

Y_pred = model.predict(X_test)

accuracy = accuracy_score(Y_test,Y_pred)
print("Accuracy:",accuracy)

#---------------step 14-----------------

cm = confusion_matrix(Y_test,Y_pred)
print(cm)

ConfusionMatrixDisplay.from_predictions(Y_test, Y_pred)

plt.title("Loan Default Confusion Matrix")
plt.show()

# -------------------step 15 -------------------

print(classification_report(Y_test,Y_pred))

#-------------------step 16 -------------------

precision = precision_score(Y_test,Y_pred)
recall = recall_score(Y_test,Y_pred)
f1 = f1_score(Y_test,Y_pred)

print("Precision:",precision)
print("Recall:",recall)
print("F1:",f1)

#---------step 17-------------------

plt.plot(model.loss_curve_)

plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.title("Training Loss Curve")

plt.show()


#------------step 18 ------------------

new_applicant = pd.DataFrame([{
    "Age": 32,
    "Income": 45000,
    "LoanAmount": 20000,
    "CreditScore": 620,
    "EmploymentYears": 5,
    "ExistingLoans": 2,
    "MonthlyDebt": 800,
    "LoanTerm": 48,
    "PreviousDefault": 1,
    "HomeOwnership_Own": 0,
    "HomeOwnership_Rent": 1
}])


new_applicant = new_applicant.reindex(
    columns=X.columns,
    fill_value=0
)

new_scaled = scaler.transform(new_applicant)

prediction = model.predict(new_scaled)[0]

if prediction == 1:
    print("High default risk")
else:
    print("Low default risk")

#----------------step 19-------------------

activations = ["identity", "logistic", "tanh", "relu"]

for activation in activations:

    model = MLPClassifier(
        hidden_layer_sizes=(32, 16),
        activation=activation,
        solver="adam",
        max_iter=1000,
        random_state=42
    )

    model.fit(X_train, Y_train)

    accuracy = model.score(X_test, Y_test)

    print(activation, accuracy)








