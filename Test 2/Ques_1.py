import pandas as pd
import matplotlib.pyplot as plt

file="100 Sales Records.csv"
df=pd.read_csv(file)
print(df.head())

col_name=df.head(0)
print(col_name)

print(df.iloc[:10,:10])

X=df['Region']
Y=df['Total Profit'].astype(float)

plt.hist(Y)

plt.ylabel('Total Profit')
plt.show()

for i in df.index:
    if(df['Total Cost'][i] > 1000000):
        print(df['Item Type'][i])