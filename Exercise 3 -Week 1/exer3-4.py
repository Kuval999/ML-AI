l1=list(input("enter list: "))
print("3rd element: ",l1[2])
print("6th element: ",l1[5])
len1=len(l1)
print(l1[:4])
print(l1[6:len1])
l1[1]='x'
l1[4]='y'
l1.pop(4)
print(l1)
print(len(l1))
