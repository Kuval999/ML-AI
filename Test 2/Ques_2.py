import pandas as pd

file="camera.csv"
df=pd.read_csv(file)
print(df.head())

print(df.head(0))
print(df.dtypes)
print(df.head(1))

print(df.iloc[:26,[0,1,12]])

print(df.describe)

