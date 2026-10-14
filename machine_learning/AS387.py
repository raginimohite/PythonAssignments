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

#separate pass students
pass_students = df[df["FinalResult"]==1]

#separate fail students
fail_students = df[df["FinalResult"]==0]

plt.scatter(pass_students["StudyHours"],pass_students["PreviousScore"],color = "green",label = "Pass")

plt.scatter(fail_students["StudyHours"],fail_students["PreviousScore"],color = "red",label = "Fail")

#Graph title
plt.title("StudyHours vs PreviousScore")

# X-axis name
plt.xlabel("Study Hours")

# Y-axis name
plt.ylabel("Previous Score")

# show legend
plt.legend()

#Display graph
plt.show()