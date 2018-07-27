from numpy import array, insert
a = ([['Rhia',10,20,30,40,50],
      ['Alan',75,80,75,85,100],
      ['Smith',80,80,80,90,95]])
a=array(a)
print(a[:3,[0,1]])

a[2]=['Sam',82,79,88,97,99]
a[0,3]=95
a= insert(a,[6],[[73],[80],[85]],axis=1)
print(a)

