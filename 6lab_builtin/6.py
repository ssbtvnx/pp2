import os
path=r"C:\giitt\6lab_builtin\w.txt"

if os.path.exists(path):
    os.remove(path)

else:
    print("there is no such a file")