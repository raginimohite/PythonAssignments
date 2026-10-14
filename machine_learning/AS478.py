from sklearn.linear_model import LinearRegression

#Dataset
X = [[1],[2],[3],[4],[5]]
Y = [50,55,60,65,70,]

#create regression model
model = LinearRegression()

#Train the model
model.fit(X,Y)

#print Coefficient
print("Coefficient:",model.coef_[0])

#print intercept
print("Intercept:",model.intercept_)

#predict marks for 6 hours
prediction = model.predict([[6]])
print("Predicted marks for 6 study hours:",prediction)
