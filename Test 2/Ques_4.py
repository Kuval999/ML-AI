import numpy as np


mat1=np.random.randint(8, size=(2,4))
print(mat1)
print("dimensions: ",mat1.shape)
print()

mat2=mat1.reshape(2,1,4)
print(mat2)
print("dimensions: ",mat2.shape)
print()


ad=np.add(mat2,5)
print("Adding: ",ad)

sub=np.add(mat2,-2)
print("subtracting: ",sub)

mul=np.multiply(mat2,5)
print("Multiplying: ",mul)