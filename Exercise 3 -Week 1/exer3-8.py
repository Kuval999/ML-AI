import math
l1=list(input("enter elements:"))
l1=list(map(int,l1))
if(len(l1)==2):
    a=l1[0]
    b=l1[1]
    res=math.fabs(((-1)*b)/a)
    print("Result: ",res)
else:
    b=l1[1]
    a=l1[0]
    c=l1[2]
    d=math.fabs((b*b)-(4*a*c))
    r1= (((-1)*b)+(math.sqrt(d)))/(2*a)
    r2= (((-1)*b)-(math.sqrt(d)))/(2*a)
    print("Result is: ",r1, " and ",r2)