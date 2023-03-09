x=input()
def polindrome(x):
    if x==x[::-1]:
        print("yes")
    else:
        print("no")

polindrome(x)