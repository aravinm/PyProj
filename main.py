
import os

directory = './data/'

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        f = open(directory + filename)
        lines = f.read()
        print (lines)

        continue
    else:
        continue



