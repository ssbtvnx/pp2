def histogram(x):
    for i in x:
        k=i #2
        while k!=0: 
            print('*',end='')
            k=k-1
        print()


print(histogram([2, 3, 4]))