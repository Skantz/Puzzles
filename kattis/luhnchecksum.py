#https://open.kattis.com/problems/luhnchecksum
n = int(input())
for _ in range(n):
    str_n = str(input().strip())
    digits_of_n = [int(e) for e in list(str_n)]
    s = 0
    for i, v in enumerate(digits_of_n[::-1]):
        if i % 2 == 0:
            s += v
            continue
        v = v * 2
        if v >= 10:
            v = int(str(v)[0]) + int(str(v)[1])
        s+= v
    if s % 10 == 0:
        print("PASS")
    else:
        print("FAIL")
