
for i in range(900,1000):
    c=0
    for j in range(2,int(i/2)):
        if(int(i%j)==0):
            c=1
            break
    if(c==0):
        temp=i
        palin=0
        while(temp>0):
            d=temp%10
            palin=(palin*10)+d
            temp=int(temp/10)
        if(i==palin):
            print(palin)
