str1=input("Enter string1: ")
str2=input("Enter string2: ")
l=tuple((set(str1)&set(str2)))
for i in l:
    print(i)