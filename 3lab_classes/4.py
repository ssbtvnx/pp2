import math
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        return self.x,self.y

    def move(self):
        self.x=int(input())
        self.y=int(input())

    def dist(self):
        d=math.sqrt((self.x**2)+(self.y**2))
        return d

a=int(input())
b=int(input())
x=Point(a,b)
print(x.dist())
x.move()
print(x.show())