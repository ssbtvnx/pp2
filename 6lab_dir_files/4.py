path=r"C:\giitt\6lab_dir_files\smth.txt"
cnt=0
smth=open(path,'r')

for i in smth:
    cnt+=1

print(cnt)