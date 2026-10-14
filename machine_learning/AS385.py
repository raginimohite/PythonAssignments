import pandas as pd

Border = "-"*30

########################################
# Step 1 : Load the dataset
########################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

Datapath = "student_performance_ml.csv"
df = pd.read_csv(Datapath)

# Average studyhours based on final result
print(df.groupby("FinalResult")["StudyHours"].mean())

# Average Attendance based on final result
print(df.groupby("FinalResult")["Attendance"].mean())
