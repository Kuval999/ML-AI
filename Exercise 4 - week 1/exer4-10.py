dic={}
for i in range(10):
    name = input('Enter Name: ')
    marks =input('Enter Marks: ')
    dic[name]=marks
import operator
sort = sorted(dic.items(), key=operator.itemgetter(1))
print('RESULT')
print('("NAME", MARKS)')
print(sort)
