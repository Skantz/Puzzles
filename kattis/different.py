#https://open.kattis.com/problems/different
import sys
for line in sys.stdin:
    line = line.split()
    a, b = int(line[0]), int(line[1])
    print(max(a, b) - min(a, b))
#Done
