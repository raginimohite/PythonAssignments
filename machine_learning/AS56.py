import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    BaggingClassifier,
    RandomForestClassifier,
    AdaBoostClassifier,
    VotingClassifier
)

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report
)

df = pd.read_csv("fraud_dataset.csv")

print(df.head())

print(df.shape)
print(df.columns)
print(df.isnull().sum())

print("\n")

le = LabelEncoder()
df["Device_Type"] = le.fit_transform(df["Device_Type"])

# Features and target

X = df.drop("Fraud",axis = 1)
Y = df["Fraud"]

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

print("Trainng data :",X_train.shape)
print("Testing data:",X_test.shape)

#---------------------------------

model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

accuracy  = accuracy_score(Y_test,Y_pred)

print("Decision tree accuracy:",accuracy)

#-----------------------------------

model = BaggingClassifier(
    n_estimators=10,
    random_state=42
)
model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)

print("Bagging accuracy:",accuracy_score(Y_test,Y_pred))

#-----------------------------------

model = RandomForestClassifier(
    n_estimators=10,
    random_state=42
)
model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)

print("random forest accuracy:",accuracy_score(Y_test,Y_pred))


#-----------------------------------

model = AdaBoostClassifier(
    n_estimators=10,
    random_state=42
)
model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)

print("AdaBoost accuracy:",accuracy_score(Y_test,Y_pred))


#-----------------------------------

dt = DecisionTreeClassifier(random_state=42)
rf = RandomForestClassifier(n_estimators=10,random_state=42)
ab = AdaBoostClassifier(n_estimators=10,random_state=42)

model = VotingClassifier(
    estimators=[("DT",dt),
                ("RF",rf),
                ("AB",ab)
                ],
                voting="hard"
)
model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)

print("voting  accuracy:",accuracy_score(Y_test,Y_pred))

print("Accuracy:", accuracy_score(Y_test, Y_pred))
print("Precision:", precision_score(Y_test, Y_pred, zero_division=0))
print("Recall:", recall_score(Y_test, Y_pred, zero_division=0))
print("F1 Score:", f1_score(Y_test, Y_pred, zero_division=0))


