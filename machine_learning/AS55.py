import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier

df = pd.read_csv("Loan_approval.csv")
print(df.head())

#-----------Step 2 :-----------------

print(df.isnull().sum())

#-----------Step 3:-----------------

X = df.drop("LoanApproved",axis=1)
Y = df["LoanApproved"]

#-----------Step 4 :----------------

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,random_state=42)

#------------Step 5 :---------------

lr_model = LogisticRegression()
lr_model.fit(X_train,Y_train)

lr_model_pred = lr_model.predict(X_test)

lr_model_acc = accuracy_score(Y_test,lr_model_pred)
print("Logistic regression:",lr_model_acc)

#-----------step 6 :------------------

dt_model = DecisionTreeClassifier()
dt_model.fit(X_train,Y_train)

dt_model_pred = dt_model.predict(X_test)

dt_model_acc = accuracy_score(Y_test,dt_model_pred)
print("Decision tree clasifier:",dt_model_acc)

#-----------step 7 :------------------

KN_model = KNeighborsClassifier()
KN_model.fit(X_train,Y_train)

KN_model_pred = dt_model.predict(X_test)

KN_model_acc = accuracy_score(Y_test,dt_model_pred)
print("KNeighbors clasifier:",KN_model_acc)

#------------Step 8 :-----------------

hard_voting = VotingClassifier(
    estimators=[
        ('lr_model',lr_model),
        ('dt_model',dt_model),
        ('KN_model',KN_model)
    ],
    voting = 'hard'
)

hard_voting.fit(X_train,Y_train)
hard_pred = hard_voting.predict(X_test)

hard_acc = accuracy_score(Y_test,hard_pred)
print("Hard voting:",hard_acc)

#-------------Step 9 :---------------

soft_voting = VotingClassifier(
    estimators=[
        ('lr_model',lr_model),
        ('dt_model',dt_model),
        ('KN_model',KN_model)
    ],
    voting = 'soft'
)

soft_voting.fit(X_train,Y_train)
soft_pred = soft_voting.predict(X_test)

soft_acc = accuracy_score(Y_test,hard_pred)
print("softrd voting:",soft_acc)













