# Deep Learning - Feed Forward Neural Network

import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# --------------------------------------------------
# 1. Create Dataset
# --------------------------------------------------

X = np.array([
    [25, 500, 12, 1, 2],
    [30, 700, 24, 0, 1],
    [45, 1200, 6, 5, 8],
    [50, 1500, 5, 6, 10],
    [28, 600, 18, 1, 1],
    [35, 800, 30, 0, 0],
    [48, 1400, 4, 7, 9],
    [52, 1600, 3, 8, 12],
    [27, 550, 20, 0, 1],
    [42, 1300, 8, 4, 7]
])

# Output
# 0 = Customer will stay
# 1 = Customer will leave

y = np.array([
    0, 0, 1, 1, 0,
    0, 1, 1, 0, 1
])

# --------------------------------------------------
# 2. Split Dataset into Training and Testing
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# --------------------------------------------------
# 3. Apply StandardScaler
# --------------------------------------------------

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# --------------------------------------------------
# 4. Create Feed Forward Neural Network
# --------------------------------------------------

model = Sequential()

# Input layer + Hidden layer
model.add(Dense(10, input_dim=5, activation='relu'))

# Second hidden layer
model.add(Dense(8, activation='relu'))

# Output layer
model.add(Dense(1, activation='sigmoid'))

# --------------------------------------------------
# 5. Compile the Model
# --------------------------------------------------

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# --------------------------------------------------
# 6. Train the Model
# --------------------------------------------------

model.fit(
    X_train,
    y_train,
    epochs=100,
    batch_size=2,
    verbose=1
)

# --------------------------------------------------
# 7. Evaluate Accuracy
# --------------------------------------------------

loss, accuracy = model.evaluate(X_test, y_test, verbose=0)

print("\nTest Accuracy:", accuracy * 100, "%")

# --------------------------------------------------
# 8. Test Input
# --------------------------------------------------

new_customer = np.array([
    [46, 1450, 5, 6, 9]
])

# Scale new customer
new_customer_scaled = scaler.transform(new_customer)

# Prediction
prediction = model.predict(new_customer_scaled)

# --------------------------------------------------
# 9. Display Result
# --------------------------------------------------

if prediction[0][0] >= 0.5:
    print("Prediction: Customer will leave")
else:
    print("Prediction: Customer will stay")