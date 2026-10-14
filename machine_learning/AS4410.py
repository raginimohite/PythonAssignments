import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name':['Amit','Sagar','Pooja'],
    'Math':[85,90,78],
    'Science':[92,88,80],
    'English':[75,85,82]
}

df = pd.DataFrame(data)

print("Dataframe:")
print(df)

print("\nShape")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nDescriptive Statistics:")
print(df.describe())

df['Total'] = df['Math'] + df['Science'] + df['English']
print(df)

print("\n")
students = df[df['Science']>85]
print(students)

print("\n")
df['Name'] = df['Name'].replace('Pooja','puja')
print(df)

print("\n")
df = df.sort_values(by='Total',ascending=False)
print(df)

plt.bar(df['Name'],df['Total'])

plt.xlabel('Students Name')
plt.ylabel('Total marks')
plt.title('Student Total Marks')


subjects = ['Math','Science','English']
marks = [85,92,75]

plt.plot(subjects,marks,marker='o')

plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title('Amits Marks')


data2 = {
    'Name': ['Amit', 'Sagar', 'Puja'],
    'Math': [None, 76, 88],
    'Science': [90, None, 85],
}
df2 = pd.DataFrame(data2)

print("Before filling missing values:")
print(df2)

df2['Math'] = df2['Math'].fillna(df2['Math'].mean())
df2['Science'] = df2['Science'].fillna(df2['Science'].mean())

print("\nAfter filling missing values:")
print(df2)

print("\n")
df = df.drop('English',axis=1)
print(df)