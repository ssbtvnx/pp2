from itertools import permutations

def permutation (x):
    perms=[''.join(p) for p in permutations(x)] #объединение списка строк 
    return perms

s=input()
result=permutation(s)

for perm in result:
    print(perm)