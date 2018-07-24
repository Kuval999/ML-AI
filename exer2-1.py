import math
n=int(input("enter the number: "))
l=len(str(n))
print(l)
temp=n
s=0
while temp > 0:
    d=temp % 10   
    s= s+ math.pow(d,l)
    temp=int(temp/10)
if(s==n):
    print("It is armstrong number")
else:
    print("It is not armstrong number")