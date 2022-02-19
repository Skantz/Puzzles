#https://open.kattis.com/problems/dasblinkenlights
import math
x, y, z = [int(e) for e in input().split()]
print("yes") if x*y/math.gcd(x, y) <= z else print("no")
#Pass
