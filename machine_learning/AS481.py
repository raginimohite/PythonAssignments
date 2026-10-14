#Dataset
X = [1,2,3,4,5]
Y = [3,4,2,4,5]

# Step 1Calculate mean of X and Y
mean_x = sum(X) / len(X)
mean_y = sum(Y) / len(Y)

print("mean of X is:",mean_x)
print("mean of Y is:",mean_y)

# Step 2 calculate slope
numerator = 0
denominator = 0

for i in range(len(X)):
    numerator = numerator + (X[i]-mean_x) * (Y[i]-mean_y)
    denominator = denominator + (X[i]-mean_x)**2

m = numerator/denominator
print("slope (m):",m)

# Calculate intercept
c = mean_y-(m * mean_x)
print("Intercept (c):",c)

#Step 4 
print("Regression equation: Y =",m,"X+",c)

#Step 5 : predict Y when X = 6
x_new = 6
predicted_y = m * x_new + c
print("Predcted Y for X:",m,x_new,":",predicted_y)
