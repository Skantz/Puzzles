inp = input().strip()
n = len(inp)
goal = n * "PER"
s = 0
for i in range(n):
    s += int(inp[i] != goal[i])
print(s)
