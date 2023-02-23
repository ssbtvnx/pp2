import math
n=int(input("Input number of sides:"))
l=int(input("Input the length of a side:"))
x=(l*l*n)/(4*(math.tan(180/math.pi)))
print(f"The area of the polygon is:{x}")