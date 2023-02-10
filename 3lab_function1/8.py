def spy_game(nums):
    l=[0,0,7,'True']
    for i in nums:
        if i==l[0]:
            l.pop(0)
    return len(l)==1

print(spy_game([1,2,4,0,0,7,5])) 
print(spy_game([1,0,2,4,0,5,7])) 
print(spy_game([1,7,2,0,4,5,0]))