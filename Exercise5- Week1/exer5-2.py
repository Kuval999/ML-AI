str1=input("Enter string1: ")
str2=input("Enter string2: ")
l=list((set(str1)&set(str2)))
for i in l:
    print(i)
