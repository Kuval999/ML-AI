import math
s=0
r1=int(input("enter starting range: "))
r2=int(input("enter endig range: "))
for i in range(r1,r2):
    sq=int(math.sqrt(i))
    if(i==sq**2):
        d=i%10
        s=s+d
        i=int(i/10)
        if(s<10):
            print("Result: ",s)
    
