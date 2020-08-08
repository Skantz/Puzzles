x, y, z, w = [int(x) for x in input().strip().split()]

if not (x and y and z) or (x + y + z) < w or w < 3:
    print("NO")

else:
    print("YES")
