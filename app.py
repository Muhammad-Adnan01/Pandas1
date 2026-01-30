import pandas as pd

# Use the full path to be sure
df = pd.read_csv(r"E:\Model Training Work\pandas\Pandas1\titanic.csv")

print(df)
print("DataFrame loaded successfully.")
print(df.shape)
print(df.columns)