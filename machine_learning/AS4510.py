import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]
}

df = pd.DataFrame(data)

df['Math_Normalized'] = (df['Math']-df['Math'].min()) / (df['Math'].max()-df['Math'].min())
print(df)

#------------------Q2-----------------------

#Create Gender column
df['Gender'] = ['Male','Male','Female']

# save for step 3
gender = df['Gender']

#One hot encoding
df = pd.get_dummies(df,columns=['Gender'])

print(df)

#-----------------Q3--------------------

#Group student by gender and calculate average marks
average_marks = df.assign(Gender=gender).groupby('Gender')[['Math','Science','English']].mean()
print("\nAverage marks by Gender:")
print(average_marks)

#-----------------Q4-------------------

# select amit marks
amit_marks = df.loc[0,['Math','Science','English']]

#Create Pie chart
plt.pie(amit_marks,labels=amit_marks.index,autopct='%1.1f%%')

plt.title("Amit's marks Distribution")
plt.show()

#---------------Q5------------------------

#Calculate total marks
df['Total'] = df['Math']+df['Science']+df['English']

#Create Pass/Fail status
df['Status'] = df['Total'].apply(lambda x: 'Pass' if x >=250 else 'Fail')

print("\n Final Dataframe:")
print(df)

#-------------------Q6---------------------

# Count number of students who passed
pass_count = (df['Status']=='Pass').sum()
print("\nNumber of students passed:",pass_count)

#------------------Q7---------------------------

#Export final dataframe to csv file
df.to_csv('final_students.csv',index=False)

print("\nDataframe successfully exported to final_students.csv :")

#---------------------Q8----------------------

#create histogram of math marks
plt.hist(df['Math'])
plt.xlabel("Math marks")
plt.ylabel('Number of students')
plt.title('Distribution of math marks')
plt.show()

#-------------------Q9------------------------

#Rename math column to mathematics
df.rename(columns={'Math':'Mathematics'},inplace=True)
print("\nDataframe after renaming column:")
print(df)

#-------------------Q10-------------------------------

#Create boxplot of english marks
plt.boxplot(df['English'])
plt.ylabel('English marks')
plt.title("Boxplot of english marks")
plt.show()