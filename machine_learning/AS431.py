import pandas as pd

# Step 1: Get data
Datapath = "MarvellousInfosystem_PlayPredictor.csv"
df = pd.read_csv(Datapath)
print(df)