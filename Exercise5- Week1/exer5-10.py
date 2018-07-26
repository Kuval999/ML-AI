f=open("f1.txt","r")
c=0
str=input("Enter a string: ")
for i in f:
    s=i.split()
    print(s)
    if str in s:
        c+=1
print("the no.of occurrences are: ",c)