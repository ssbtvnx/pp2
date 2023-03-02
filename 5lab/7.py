import re
def t(text):
    y=re.sub("_"," ", text)
    y=y.title()
    y=re.sub(" ","", y)
    return y
    
text=input()
print(t(text))