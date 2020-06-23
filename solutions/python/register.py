# https://open.kattis.com/problems/register

from functools import reduce

current = list(map(int,input().split()))
diffs = [[2, 3, 5, 7, 11, 13, 17, 19][i] - current[i] for i in range(8)]
"""
print(reduce(lambda x,y: x*y, diffs) -1)
"""

s = 1
for d in diffs:
  s *= d
print(s)
