f=open("f1.txt","a")
str=input("Enter a string: ")
f.write(str)
f.close()
f1=open("f1.txt","r")
for i in f1:
    print(i)