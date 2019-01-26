
import os

directory = './data/'

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        with open(directory + filename) as f:
            lines = f.read()
            print (lines)
            close(f)
        continue
    else:
        continue



