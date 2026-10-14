import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#Dataset
X = np.array([[1],[2],[3],[4],[5]])
Y = np.array([20000,25000,30000,35000,40000])

#Step 1: Create Linear Rgressio model
model = LinearRegression()

# Step 2: Train the model
model.fit(X,Y)

#Step 3: Predict salary for 6 years of experience
experience = np.array([[6]])
predicted_salary = model.predict(experience)

print("Predicted salary for 6 years Experience:",predicted_salary[0])

#predicted salary for graph
Y_pred = model.predict(X)

#STep 5: plot data points
plt.scatter(X,Y,label ="Data Points")

#Step 6: plot regression line
plt.plot(X,Y_pred,label ="Regression Line")

#labels and titles
plt.xlabel("Years of experience")
plt.ylabel("Salary")
plt.title("Experience vs Salary")

plt.legend()
plt.show()