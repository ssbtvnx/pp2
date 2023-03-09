import os

if os.path.exists("removed.txt"):
    os.remove("removed.txt")
else:
    print("there is no file")