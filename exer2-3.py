s=input("enter string:")
print("Length: ",len(s))
a=d=u=l=0
for i in range(0,len(s)):
    if s[i].isalpha(): a=a+1
    if s[i].isdigit(): d=d+1
    if s[i].isupper(): u=u+1
    if s[i].islower(): l=l+1
    
print("no.of upper case: ",u)
print("no.of lower case: ",l)
print("no.of character: ",a)
print("no.of digits: ",d)

s1= input("enter the string to add ing: ")
print(s1+ "ing")

s2= input("enter the string for changing the occurence: ")
r=s2[0]
s2=s2.replace(r,'$')
s2=s2.replace('$',r,1)
print(s2)

    