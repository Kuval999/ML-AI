d={}
for i in range(5):
    key=input("enter key: ")
    val=int(input("enter val: "))
    d[key]=val
print(sum(d.values()))