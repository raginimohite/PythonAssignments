# Program to calculate loss manually

import math

# Actual and predicted values
actual = [1, 0, 1, 1]
predicted = [0.9, 0.2, 0.8, 0.7]

# Number of values
n = len(actual)

# -----------------------------
# 1. Mean Squared Error (MSE)
# -----------------------------

mse = 0

for i in range(n):
    error = actual[i] - predicted[i]
    mse = mse + error ** 2

mse = mse / n

print("Mean Squared Error (MSE) =", mse)


# --------------------------------
# 2. Binary Cross Entropy (BCE)
# --------------------------------

bce = 0

for i in range(n):
    y = actual[i]
    p = predicted[i]

    bce = bce + (y * math.log(p) + (1 - y) * math.log(1 - p))

bce = -bce / n

print("Binary Cross Entropy (BCE) =", bce)