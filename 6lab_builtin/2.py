x=input()
def calculate(x):
    cnt1=0
    cnt2=0
    for i in x:
        if i.isupper():
             cnt1+=1
        if i.islower():
             cnt2+=1
    print(cnt1)
    print(cnt2)

calculate(x)