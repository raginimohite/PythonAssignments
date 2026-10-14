# Deep Learning - Feed Forward Neural Network

import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# --------------------------------------------------
# 1. Create Dataset
# --------------------------------------------------

X = np.array([
    [25000, 600, 200000, 10000, 0],
    [40000, 700, 300000, 8000, 1],
    [60000, 750, 500000, 12000, 1],
    [20000, 550, 150000, 15000, 0],
    [80000, 800, 700000, 5000, 1],
    [35000, 650, 250000, 9000, 1],
    [18000, 500, 100000, 12000, 0],
    [90000, 850, 800000, 15000, 1],
    [30000, 580, 200000, 14000, 0],
    [70000, 780, 600000, 10000, 1]
])


# Output
# 0 = Loan rejected
# 1 = Loan approved

y = np.array([
    0, 1, 1, 0, 1,
    1, 0, 1, 0, 1
])


# --------------------------------------------------
# 2. Split Dataset
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
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

# Input Layer + Hidden Layer
model.add(Dense(10, input_dim=5, activation='relu'))

# Second Hidden Layer
model.add(Dense(8, activation='relu'))

# Output Layer
model.add(Dense(1, activation='sigmoid'))


# --------------------------------------------------
# 5. Compile Model
# --------------------------------------------------

model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)


# --------------------------------------------------
# 6. Train Model
# --------------------------------------------------

model.fit(
    X_train,
    y_train,
    epochs=100,
    batch_size=2,
    verbose=1
)


# --------------------------------------------------
# 7. Evaluate Model
# --------------------------------------------------

loss, accuracy = model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print("Test Accuracy:", accuracy * 100, "%")


# --------------------------------------------------
# 8. Test Input
# --------------------------------------------------

new_applicant = np.array([
    [55000, 720, 400000, 10000, 1]
])


# Scale new applicant
new_applicant_scaled = scaler.transform(new_applicant)


# --------------------------------------------------
# 9. Prediction
# --------------------------------------------------

prediction = model.predict(
    new_applicant_scaled,
    verbose=0
)


# --------------------------------------------------
# 10. Display Result
# --------------------------------------------------

if prediction[0][0] >= 0.5:
    print("Prediction: Loan Approved")
else:
    print("Prediction: Loan Rejected")