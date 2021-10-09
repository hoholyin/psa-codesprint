import re

f = open("emotions.txt", "r")
for l in f:
    if "/" in l or len(l) == 0:
        continue
    else:
        allwords = l.split(" ")
        for w in allwords:
            print(w.rstrip())
