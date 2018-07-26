s={"a","e","i","o","u"}
print(s)
c=0
str=input("enter a string: ")
for i in str:
    if i in s:
        c+=1
print("The no.of vowels is: ",c)
