import pandas as pd

data ={
    'Name': [' Alice ', ' Bob', 'Charlie ', ' David'],
    'Age': [25, None, 30, 22],
    'salary': [70000, 80000, None, None]
}

df= pd.DataFrame(data)

# 1. Remove leading and trailing whitespace from string columns
print("Original DataFrame:")
print(df)

print(df.isnull().sum())
df_dropped = df.dropna()

print("\nDataFrame after dropping rows with missing values:")
print(df_dropped)


df['Age'] = df['Age'].fillna(df['Age'].mean())
df['salary'] = df['salary'].fillna(df['salary'].mean())
print(df['Age'].mean())
print(df['salary'].mean())
print(df)