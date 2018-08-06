import pandas as pd

f="file.xlsx"
df=pd.read_excel(f)
print(df.head())

sorted_height=df.sort_values(['Height'], ascending=True)
print(sorted_height)

df['BMI']=df['Weight']/pow((df['Height']*0.3048),2)
print(df)

print("Grouping: ",df.groupby('BMI'))

h=df[(df.BMI>=15) & (df.BMI<=20)]
print(" Healthy weight: ",h['Name'].to_string(index=False))

ov=df[(df.BMI> 20) & (df.BMI<=29)]
print(" Overweight: ",ov['Name'].to_string(index=False))

ob=df[(df.BMI>=30)]
print(" Obese: ",ob['Name'].to_string(index=False))