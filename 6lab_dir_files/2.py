import os

print('Exist:', os.access('C:\giitt', os.F_OK))
print('Readable:', os.access('C:\giitt', os.R_OK))
print('Writable:', os.access('C:\giitt', os.W_OK))
print('Executable:', os.access('C:\giitt', os.X_OK))