n=int(input("enter a number:"))
f=1
while (n>0):
        f=f * (n)
        n=n-1
print("Factorial: ",f)

num=int(input("enter limit for fibonacci: "))
print('  0')
print('  1') 
a=0
b=1
while(num>0):
    c=a+b
    a=b
    b=c
    print(" ",c)
    num-=1
    
    
