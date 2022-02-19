#https://open.kattis.com/problems/pieceofcake2
a, b, c = [int(e) for e in input().strip().split()]
x1, x2 = b, a - b
y1, y2 = c, a - c

sq1 = max(x1, x2) * max(y1, y2)

print(max(4*sq1, 4*sq1))
#Done
