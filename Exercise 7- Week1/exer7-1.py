import math
for i in range(1,1000):    
    l=len(str(i))
    s=0
    temp=i
    while i > 0:
        d=i % 10   
        s= s+ math.pow(d,l)
        i=int(i/10)
    if(s==temp):
        print(temp)
