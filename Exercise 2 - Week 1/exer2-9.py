str=input("Enter the string:")
c=0
l=len(str)
for i in range(0,l):
    print("Index of :",str[i]," is ",i)
    if(str[i]== 'a' or str[i]== 'o' or str[i]== 'i' or str[i]== 'e' or str[i]== 'u'):
        c+=1;
print("No.of vowels: ",c)
