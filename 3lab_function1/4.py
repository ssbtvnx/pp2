def prime(a):
    if(a==1): return False
    if(a==2): return True
    if(a%2==0): return False

    p= int(a**0.5)+1
    for i in range(3,p):
        if(a%i==0): return False
    return True

def filter_prime(n):
    filtered_list=[]
    for i in n:
        if(prime(i)):
            filtered_list.append(i)
    return filtered_list

x=list(map(int, input().split()))
b=filter_prime(x)
print(*b)