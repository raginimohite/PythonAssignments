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

plt.scatter(df["SleepHours"],df["FinalResult"])

plt.title("sleep hour vs final result")

plt.xlabel("Sleep hours")

plt.ylabel("Final result")

plt.show()