#Dataset
X = [1,2,3,4,5]
Y = [3,4,2,4,5]

#Regression equation from question 1
m = 0.4
c = 2.4

#Step 1 : Predicted Y values
predicted_y = []

for x in X:
    y_pred = m * x + c
    predicted_y.append(y_pred)

    print("Actual Y   Predicted Y")
    for i in range(len(Y)):
        print(Y[i],"     ",predicted_y[i])

# Step 2: Calculate MSE
squared_error = []

for i in range(len(Y)):
    error = Y[i]-predicted_y[i]
    squared_error.append(error ** 2)

mse = sum(squared_error)/len(Y)

print("\nSquared Errors =",squared_error)
print("MSE =",mse)

#Step 3 ; Calculate R2 score
mean_y = sum(Y) / len(Y)

ss_total = 0
ss_residual = 0

for i in range(len(Y)):
    ss_total = ss_total + (Y[i]-mean_y)**2
    ss_residual = ss_residual + (Y[i]-predicted_y[i] ** 2)

r2 = 1- (ss_residual/ss_total)

print("SS Total =",ss_total)
print("SS Residual =",ss_residual)
print("R2 Score =",r2)

