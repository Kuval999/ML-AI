l1=list(input("Enter list: "))
l2=list(input("Enter list: "))
s1=set(l1)
s2=set(l2)
i=s1.intersection(s2)
u=s1.union(s2)
print("Intersection: ",list(set(i)))
print("union: ",list(set(u)))