n=['','','','','','','','','','']
s1=['','','','','','','','','','']
s2=['','','','','','','','','','']
s3=['','','','','','','','','','']

for i in range(10):
    n[i]=input("enter name: ")
    s1[i]=int(input("Enter sub1 marks: "))
    s2[i]=int(input("Enter sub2 marks: "))
    s3[i]=int(input("Enter sub3 marks: "))
print("NAME \t SUB1 \t SUB2 \t SUB3")
for i in range(10):
    print(n[i],'\t',s1[i],'\t',s2[i],'\t',s3[i])
    
m1=(s1[0]+s1[1]+s2[2])/3
m2=(s2[0]+s2[1]+s2[2])/3
m3=(s3[0]+s3[1]+s3[2])/3
print(" Mean for sub 1: ", m1)
print(" Mean for sub 2: ", m2)
print(" Mean for sub 3: ", m3)

print(" Median for sub1:" , int(((s1[5]+s1[6])/2)))
print(" Median for sub1:" , int(((s2[5]+s2[6])/2)))
print(" Median for sub1:" , int(((s2[5]+s2[6])/2)))

for i in range(3):
    s=((s1[i]+s2[i]+s3[i])*100)/3
    if(s>90):
        print(n[i], ": Grade A+")
    elif(s>80): print(n[i], ": Grade A")
    elif(s>70): print(n[i], ": Grade B+")
    elif(s>60): print(n[i], ": Grade B")
    elif(s>50): print(n[i], ": Grade C")
    else: 
        print(n[i], ": Grade D")
        
