#https://open.kattis.com/problems/dirtydriving

inp = input().split()
n, p = int(inp[0]), int(inp[1])
distances = list(map(int,input().split()))
distances.sort()

f_x = lambda p, n: p*(n+1)

ys  = [f_x(p, distances.index(x))-x+1 for x in distances]

print(max(ys))
