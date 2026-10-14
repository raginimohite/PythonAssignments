import pandas as pd

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

