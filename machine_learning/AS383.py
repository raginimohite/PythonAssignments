import pandas as pd

Border = "-"*30

########################################
# Step 1 : Load the dataset
########################################

print(Border)
print("Step 1 : calculate and display")
print(Border)

Datapath = "student_performance_ml.csv"
df = pd.read_csv(Datapath)

print("Average study hours:",df["StudyHours"].mean())

print("Average Attendance:",df["Attendance"].mean())

print("maximum previous score:",df["PreviousScore"].max())

print("minimum sleep hours:",df["SleepHours"].min())