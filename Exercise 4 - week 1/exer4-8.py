str=input("enter sentence: ")
str=str.split()
d={}
for i in str:
    count=0
    for j in str:
        if(i==j):
            count=count+1
    d[i]=count
print(d)
