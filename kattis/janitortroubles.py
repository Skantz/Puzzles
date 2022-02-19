#https://open.kattis.com/problems/janitortroubles
a, b, c, d = [int(e) for e in input().strip().split(" ")]
s = (a + b + c + d) / 2
print(((s - a) * (s - b) * (s - c) * (s - d))**0.5)
#Finished
