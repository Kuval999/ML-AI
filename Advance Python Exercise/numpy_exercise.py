import numpy as np
r=int(input("Enter no.of rows: "))
c=int(input("Enter no.of cols: "))

def accept(r,c):    
    a=[]
    for i in range(r):
        b=[]
        for j in range(c):
            ele=int(input("Enter element: "))
            b.append(ele)
        a.append(b)
    return a
    
mat1=np.array(accept(r,c))
print(mat1)

print(mat1.reshape(c,r))

print(mat1[0:2,1])

print(mat1.flatten())

print(np.sum(mat1))

print(mat1.max())

print(mat1.min())

mat2=np.array(accept(r,c))

s1=np.add(mat1,mat2)
print(s1)

m1=np.multiply(mat1,mat2)
print(m1)

d1=np.divide(mat1,mat2)
print(d1)