f=open("f1.txt","r")

for i in f:
    print(i)
    w=i.split()
    for j in w:
        print(j.capitalize())
        #j.capitalize()
    
#print("the no.of occurrences are: ",c)
