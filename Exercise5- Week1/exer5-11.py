f=open("f1.txt","r")
f1=open("f2.txt","w")
for i in f:
    f1.write(i)
f1.close()
f.close()
f1=open("f1.txt","r")
for i in f1:
    print(i)