import os

e = []
mask = ['O', 'P', 'K']
b = []
cwd = os.getcwd()

for file in os.listdir(cwd):
    if file.startswith("ОРК"):
        e += file
        b = mask + e[3:]
        b = ''.join(b)
        os.rename(file, b)
        b = []
        e = []
