import pandas as pd
import matplotlib.pyplot as plt

Border = "-"*30

########################################
# Step 1 : Load the information
########################################

print(Border)
print("Step 1 : Load the boxplot")
print(Border)

Datapath = "student_performance_ml.csv"
df = pd.read_csv(Datapath)

#Draw Boxplot
plt.boxplot(df["Attendance"])

#Give Title
plt.title("Boxplot of Attendance")

#Give y axis label
plt.ylabel("Attendance")

#Display graph
plt.show()