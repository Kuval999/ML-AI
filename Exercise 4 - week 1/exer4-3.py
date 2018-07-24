d={1:'a',2:'b',3:'c'}
key=int(input("Enter key to check:"))
if key in d.keys():
      print("Key is present: ",key,d[key])
else:
      print("Error message")
