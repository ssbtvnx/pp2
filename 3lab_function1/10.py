def unique(x):
    list=[]
    for i in x:
        if i not in list:
            list.append(i)
    return list

print(unique([1,4,5,4,5,6,7]))