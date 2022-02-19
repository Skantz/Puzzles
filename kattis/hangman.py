w = set(list(input().strip()))
g = set(list(input().strip())[:10 + len(w) - 1])
print("WIN") if w - g == set() else print("LOSE")
