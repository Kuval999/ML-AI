import re
p=input("enter the password: ")
print(p)
flag = 0
while True:  
    if (len(p)<8):
        flag = -1
        break
    elif not re.search("[A-Z]", p):
        flag = -1
        break
    elif not re.search("[0-9]", p):
        flag = -1
        break
    elif not re.search("[^a-zA-Z0-9]", p):
        flag = -1
        break
    elif len(p)>=14:
        flag = -1
        break
    else:
        flag = 0
        print("Valid Password")
        break
 
if flag ==-1:
    print("Not a Valid Password")