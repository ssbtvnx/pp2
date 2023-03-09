import math
list=[]
x=int(input())
for i in range(x):
    i=int(input())
    list.append(i)
y=math.prod(list)

print(y)