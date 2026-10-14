from sklearn.metrics import classification_report,accuracy_score

actual = [1,1,1,1,0,0,0,0]
predicted = [1,1,0,1,0,1,0,0]

print("Classification Report :")
print(classification_report(actual,predicted))

accuracy = accuracy_score(actual,predicted)

print("Accuracy=",accuracy)