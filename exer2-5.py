str=input("Enter the string:")
l=len(str)
c=0
str1=""
for i in range(0,l):
    if(i%2==0):
        str1=str1+str[i]
print(str1)

a=str.split(" ")
d=dict()
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d:
    print(i,d[i])
        
