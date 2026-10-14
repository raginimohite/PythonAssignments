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

print("pass and fail counts")
print(df["FinalResult"].value_counts())

# Dataset is balanced
print("\n pass and fail percentage")
print(df["FinalResult"].value_counts(normalize=True) * 100)

