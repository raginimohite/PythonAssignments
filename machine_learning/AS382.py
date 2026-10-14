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

# Display total number of students
print("Total Students :", len(df))

# Display number of passed students
print("Passed Students :", (df["FinalResult"] == 1).sum())

# Display number of failed students
print("Failed Students :", (df["FinalResult"] == 0).sum())