print("Enter:")
x=""
while True:
    try:
        str=input()
        x=x+"ABC "+str+'\n'
    except EOFError:
        break
print(x)
