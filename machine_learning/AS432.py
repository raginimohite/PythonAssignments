import pandas as pd
#step 2
from sklearn.preprocessing import LabelEncoder

# Step 1: Get data
Datapath = "MarvellousInfosystem_PlayPredictor.csv"
df = pd.read_csv(Datapath,sep="\t")
print(df)

# Step 2 : Clean prepare and manipulate data
le = LabelEncoder()

df["Wether"] = le.fit_transform(df["Wether"])
df["Temperature"] = le.fit_transform(df["Temperature"])
df["Play"] = le.fit_transform(df["Play"])

print("\nEncoded Data:")
print(df)




