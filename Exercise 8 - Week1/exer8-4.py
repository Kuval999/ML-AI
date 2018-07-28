a1=int(input("Enter order of row of first matrix :"))
b1=int(input("Enter order of col of first matrix :"))
a2=int(input("Enter order of row of second matrix :"))
b2=int(input("Enter order of col of second matrix :"))
m1 = [[0]*b1 for i in range(a1)]
m2 = [[0]*b2 for row in range(a2)]
res = [[0]*b2 for row in range(a1)]
print(res)

if(a2!=b1):
    print("The matrices cannot be multiplied")
else:
    print("enter elements of the first matrix: ")
    for i in range(a1):
        for j in range(b1):
             m1[i][j]=int(input())
    print("enter elements of the second matrix: ")
    for i in range(a2):
        for j in range(b2):
             m2[i][j]=int(input())
    
    for i in range(a1):
        for j in range(b2):
            for k in range(b1):
                res[i][j]+=m1[i][k]*m2[k][j]

    print(res)