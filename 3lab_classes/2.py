class Shape():
    def __init__(self):
        pass
class Square(Shape):
    def __init__(self,length):
        self.length=length
    def Area(self):
        area=self.length**2
        return area
    
x=int(input())
a=Square(x)
print(a.Area())