import re
text=input()
y=re.sub(r"([A-Z])", r" \1", text)
print(y)