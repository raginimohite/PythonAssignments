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


plt.hist(df["StudyHours"], bins = 10)

# Give title
plt.title("Histogram of study hours")

# X-axis name
plt.xlabel("Study Hours")

# Y-axis name
plt.ylabel("Number of students")

#Display graph
plt.show()