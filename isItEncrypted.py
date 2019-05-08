import os

def read_file(file):
    with open(file) as f:
        SMRF1 = f.readlines()
    return SMRF1

def itIsEncrypted(file):
    print('someone is trying to encrypt your file:')
    print(file)

def isItEncrypted(file):
    initial = read_file(file)
    while True:
        current = read_file(file)
        if initial != current:
            for line in current:
                if line not in initial:
                    itIsEncrypted(file)
            #initial = current
        current=initial


path = input("Please enter the path of the folder you would like to protect: ")
files = []
# r=root, d=directories, f = files
for r, d, files in os.walk(path):
    for file in files:
        if '.txt' in file:
            files.append(os.path.join(r, file))
while True:
    for file in files:
        isItEncrypted(file)
        
#since the encryption can be partitial, and in any possible way, i decided to check only if the files were changed..
