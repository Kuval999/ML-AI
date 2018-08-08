import pandas as pd
#from sklearn.datasets import load_boston

file='boston.xls'
df = pd.read_excel(file)
print(df.head())

columnNames = list(df.head(0)) 
print(columnNames[0:2])


print("data types of all columns: ")
print(df.dtypes)
print()

print("maximum value in column 1: ")
print(df[columnNames[1]].max())

print("minimum value in column 1: ")
print(df[columnNames[1]].min())