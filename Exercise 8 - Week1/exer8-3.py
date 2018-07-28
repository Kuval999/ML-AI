t1=tuple(int(t.strip()) for t in input("enter weight: ").split(','))
print(t1)
t2=tuple(int(t.strip()) for t in input("enter height: ").split(','))
for i in range(len(t1)):
    bmi=t1[i]/(t1[i]**2)
    print("The BMI's of the students are: ",bmi)