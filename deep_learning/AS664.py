# Program to show how weights are updated in ANN

# Take input, weight, bias, target output and learning rate
input_value = 2
weight = 0.5
bias = 0.1
target = 1
learning_rate = 0.1

# Store old weight
old_weight = weight

# Step 1: Calculate prediction
prediction = (input_value * weight) + bias

# Step 2: Calculate error
error = target - prediction

# Step 3: Update weight using gradient descent logic
weight = weight + (learning_rate * error * input_value)

# Display results
print("Input =", input_value)
print("Bias =", bias)
print("Target Output =", target)
print("Learning Rate =", learning_rate)

print("\nPrediction =", prediction)
print("Error =", error)

print("\nOld Weight =", old_weight)
print("Updated Weight =", weight)