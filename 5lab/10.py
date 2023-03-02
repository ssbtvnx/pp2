import re
def f(Object):
    return Object.group("a1")+ "_" + Object.group("a2").lower()

text=input()
y=re.sub(r"(?P<a1>[a-z])(?P<a2>[A-Z])+", f, text)
print(y)