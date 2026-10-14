from sklearn.linear_model import LinearRegression

#Dataset

#input features
X = [
    [1,7],
    [2,6],
    [3,7],
    [4,6],
    [5,8]
]

#Target variables
Y = [50,55,60,65,70,]

#create regression model
model = LinearRegression()

#Train the model
model.fit(X,Y)

#print Coefficient
print("Coefficient for studyHours:",model.coef_[0])
print("Coefficient for sleepHours:",model.coef_[1])


#print intercept
print("Intercept:",model.intercept_)


