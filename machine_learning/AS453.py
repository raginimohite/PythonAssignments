import pandas as pd

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

#Step 3
#Group student by gender and calculate average marks
average_marks = df.assign(Gender=gender).groupby('Gender')[['Math','Science','English']].mean()
print("\nAverage marks by Gender:")
print(average_marks)