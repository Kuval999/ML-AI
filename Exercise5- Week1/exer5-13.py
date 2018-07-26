f=open("f1.txt","r")
for i in f:
    w=i.split()
    for j in w:
        for k in j:
            if k.isdigit():
                print(k)         