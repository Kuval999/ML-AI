f=open("f1.txt","r")
c=0
str=input("Enter letter to be searched for: ")
for i in f:
    w=i.split()
    print(w)
    for j in w:
        print(j)
        for k in j:
            if str in k:
                c+=1
print("the no.of occurencesx are: ",c)              