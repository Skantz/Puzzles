import sys

queens_n = int(input())

queens_pos = []

for _ in range(queens_n):
  inp = input().split()
  queens_pos.append( (int(inp[0]), int(inp[1])) )

row_plus_col  = [q[0] + q[1] for q in queens_pos]
row_minus_col = [q[0] - q[1] for q in queens_pos]

row_sum       = [q[0] for q in queens_pos]
col_sum       = [q[1] for q in queens_pos]

correct = 1

for check in [row_plus_col, row_minus_col, row_sum, col_sum]:
  if max([check.count(item) for item in check]) > 1:
    correct = 0
    break

print("CORRECT") if correct else print("INCORRECT")
