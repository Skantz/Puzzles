#https://open.kattis.com/problems/freefood
import sys
days = set()
for i, line in enumerate(sys.stdin):
    if i == 0:
        n = int(line.strip())
        continue
    start, end = line.strip("\n").split(" ")
    for j in range(start, end + 1):
        days.add(j)
print(len(days))
#Finished
