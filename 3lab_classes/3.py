class Shape():
    def __init__(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def Area(self):
        area=self.length*self.width
        return area

x=int(input())
y=int(input())
a=Rectangle(x,y)
print(a.Area())