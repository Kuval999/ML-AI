str=input("Enter a string: ")
cn=0
cl=0
for i in str:
    if(i.isdigit()):
        cn+=1
    if(i.isalpha()):
        cl+=1
print("The no.of letters: ",cl)
print("The no.of digits: ",cn) 