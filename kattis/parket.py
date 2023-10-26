#https://open.kattis.com/problems/parket

import sys
r, b = [int(e) for e in sys.stdin.readline().split() if e.isdigit()]

candidate_coordinates_for_r = []
for i in range(0, r + 1):
    for j in range(0, r + 1):
        #print(2*i + 2*j - 4, r)
        if 2*i + 2*j - 4 == r:
            candidate_coordinates_for_r.append((i, j))

print(candidate_coordinates_for_r)
for x, y in candidate_coordinates_for_r:
    if (x - 2) * (y - 2) == b:
        print(max(x, y), min(x, y))
        break


#Passes
