print("1.FActorial")
print("2.LCM")
print("3.HCM")
print("4.Factor")
ch = int(input("Enter choice: "))
if(ch== 1):
    a = int(input("Enter number: "))
    f= 1
    while(a>0):
        f=*a;
        a = a-1
    print(f," is the factorial")
elif(ch== 2):
    a = int(input("Enter number1: "))
    b = int(input("Enter number2: "))
    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1, smaller+1):
        if((a % i == 0) and (b % i == 0)):
            hcf = i
    print(hcf)
elif(ch==3):
    x = int(input("Enter number1: "))
    y = int(input("Enter number2: "))
    if x > y:
       greater = x
    else:
       greater = y
    while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
    print(lcm)
elif(ch==4):
    a = int(input("Enter number: "))
    print("The factors are: ")
    for i in range(1, a + 1):
       if a % i == 0:
           print(i)