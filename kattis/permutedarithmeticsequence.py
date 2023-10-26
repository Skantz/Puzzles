
from copy import deepcopy

n = int(input())

for _ in range(n):
  seq = list(map(int,input().strip().split()))[1:]
  seq2 = deepcopy(seq)
  seq2.sort()
  seq3 = deepcopy(seq)
  seq3.sort()
  seq3.reverse()
  if seq == seq2 or seq == seq3:
    possible_arithmetic = 1
  else:
    possible_arithmetic = 0
  diff = seq2[1] - seq2[0]
  same_diff = 1
  for i in range(1, len(seq2)):
    if seq2[i] - seq2[i-1] != diff:
      same_diff = 0
      break
  if same_diff:
    if possible_arithmetic:
      print("arithmetic")
    else:
      print("permuted arithmetic")
  else:
    print("non-arithmetic")
