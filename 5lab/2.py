import re
text=input()
x=("ab{2,3}")
y=re.findall(x,text)
print(y)