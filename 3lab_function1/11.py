def is_palindrome(x):
    if x==x[::-1]:
        return True
    else:
        return False

x=input()
print(is_palindrome(x))