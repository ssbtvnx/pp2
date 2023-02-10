class Baisal():
    def __init__(self):
        self.s=""
    def getstring(self):
        self.s=str(input())
    def printstring(self):
        return self.s.upper()

x=Baisal()
x.getstring()
print(x.printstring())