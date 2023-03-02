import re
text=input()
x=("ab*")
y=re.search(x,text)
if y:
    print("yes")
else:
    print("no")