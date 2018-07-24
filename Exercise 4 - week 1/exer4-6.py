d={}
pro=1
for i in range(5):
    key=input("enter key: ")
    val=int(input("enter val: "))
    d[key]=val
for i in d:
    pro=pro*d[i]
print("Product: ",pro)