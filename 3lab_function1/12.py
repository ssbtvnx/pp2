def histogram(x):
    for i in x:
        a=i #2
        while a!=0: 
            print('*',end='')
            a=a-1
        print()


print(histogram([2, 3, 4]))