str="#Python is an interpreted high level programming language for general-purpose programming* ."
str=list(str)
for i in str:
    if i in "#_.,/';<>?:*":
        str.remove(i)
str=''.join(str)
print(str)

str=str.split()
for i in str:
    p=i[::-1]
    if(i==p):
        print(i)

for i in str:
    c=0
    for j in str:
        if(i==j):
            c+=1
print(c,i)     
    