n=[1,2,3,40,5,6,10,3]
n.sort()
l=len(n)
print("First largest: ",n[l-1])
print("Second largest: ",n[l-2])

temp=n[0]
n[0]=n[l-1]
n[l-1]=temp
print("After swapping: ",n)
