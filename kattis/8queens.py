rows = set()
cols = set()
diag = set()
antidiag = set()
for i in range(8):
    l = input().strip()
    for j in range(8):
        if l[j] != "*": continue
        rows.add(i)
        cols.add(j)
        diag.add(i + j)
        antidiag.add(i - j)
conflict = False
for s in [rows, cols, diag, antidiag]:
    if len(s) < 8:
        conflict = True
        break
if (not conflict): print("valid")
if conflict: print("invalid")