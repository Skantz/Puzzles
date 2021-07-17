import sys

L = int(sys.stdin.readline())
D = int(sys.stdin.readline())
X = int(sys.stdin.readline())

def digit_sum(n, sum = 0):
  if n == 0:
    return sum
  sum += n % 10
  sum = digit_sum(n//10, sum)
  return sum

min_bound = float('inf')
max_bound = 0

for i in range(L, D+1):
  if digit_sum(i) == X and i < min_bound:
    min_bound = i
  if digit_sum(i) == X and i > max_bound:
    max_bound = i


print(min_bound)
print(max_bound)
