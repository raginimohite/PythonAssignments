import pandas as pd
import matplotlib.pyplot as plt

Border = "-"*30

########################################
# Step 1 : Load the information
########################################

print(Border)
print("Step 1 : Load the dataset")
print(Border)

Datapath = "student_performance_ml.csv"
df = pd.read_csv(Datapath)

plt.scatter(df["AssignmentsCompleted"],df["FinalResult"])

plt.title("Assignment acompleted vs final result")

plt.xlabel("Assignment completed")

plt.ylabel("Final result")

plt.show()