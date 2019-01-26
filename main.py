import os
import analyser

directory = './data/'

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        with open(directory + filename) as f:
            lines = f.read()
            print (lines)
            f.close()
        continue
    else:
        continue


print analyser.best_match_for("1.txt", path=directory)
