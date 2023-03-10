def smth():
    x=int(input())
    y=(int(i) for i in range (x, 0, -1))
    for i in range(x):
        print(next(y))
smth()