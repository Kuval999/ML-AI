str1=input("enter the string: ")
print(str1)
v=u=l=s=0
str1=str1.split('.')
for i in str1:
    print(i)
    
str1[2]="UST Global specializes in Healthcare, Retail & Consumer Goods, Banking and Financial Services, Telecom, Media, & Technology, Insurance, Transportation & Logistics, and Manufacturing & Utilities."
print(str1)
vowels=['a','e','i','o','u','A','E','I','O','U']
special=['.',',','?','$','@','&','#']
count={}
for i in str1:
    c=0
    for j in i:
        if j.isupper():
            u+=1
        if j.islower():
            l+=1
        if j in special:
            s+=1
        if j in vowels:
            v+=1
'''w=str1.split()
for k in w:
    for m in w:
        if(k==m):
            c+=1
    count[k]=c'''

print("upper: ",u)
print("lower: ",l)
print("vowels: ",v)
print("sepcial: ",s)
print()
print(count)
'''str1=''.join(str1)
print(str1)
str2=re.sub('[^ a-zA-Z0-9]', '', str1)
print(str2)
'''
'''for i in str:
    for j in i:
        if j in special:
            print(j)
            i.remove(j)
print(str)'''

print()
l=len(str1)
temp=str1[0]
str1[0]=str1[l-1]
str1[l-1]=temp
print(str1)         