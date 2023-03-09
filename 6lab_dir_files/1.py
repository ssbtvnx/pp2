import os

path = "C:\giitt"

files_directories=os.listdir(path)

for i in files_directories:
    if os.path.isdir(os.path.join(path,i)):
        print(i)

print()

for i in files_directories:
    if os.path.isfile(os.path.join(path,i)):
        print(i)

print()

for i in files_directories:
    print(i)