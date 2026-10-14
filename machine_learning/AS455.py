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