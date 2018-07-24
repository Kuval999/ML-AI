l1=list(input("enter list: "))
l1=list(map(int,l1))
c=0
num=int(input("enter number to be searched: "))
for i in l1:
    if(num==i):
        c+=1;
print("The no.of times the number occured in the list is: ",c)

even=0
odd=0
for i in range(len(l1)):
    if(((l1[i]%2)==0) & l1[i]>even): even=l1[i]
    if(((l1[i]%2)!=0) & l1[i]>odd): odd=l1[i]

print("Largest even number :",even)
print("Largest odd number :",odd)

