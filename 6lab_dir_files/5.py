path=r"C:\giitt\6lab_dir_files\smth.txt"

smth=open(path,'a')
x=["\n","21 ", "Savage"]

for i in x:
    smth.write(i)
smth.close()

smth=open(path,'r')
print(smth.read())