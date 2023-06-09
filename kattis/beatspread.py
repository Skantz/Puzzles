n = int(input())
for _ in range(n):
    x, y = [int(inp) for inp in input().split()]
    if x < y or (x + y) % 2:
        print("impossible")
        continue
    print((x + y)//2, x - (x + y)//2)
