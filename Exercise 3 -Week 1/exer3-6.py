l1=list(input("enter list: "))
l1=list(map(int,l1))
l2=list()
for i in range(len(l1)):
    l2.append(l1[i]**2)
print(l2)
tup=list(zip(l1,l2))
tup.sort()
print(tup)
