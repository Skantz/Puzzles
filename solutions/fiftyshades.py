#https://open.kattis.com/problems/fiftyshades
c = len([e for e in [input().strip().lower() for _ in range(int(input()))] if "rose" in e or "pink" in e])
print(c) if c > 0 else print("I must watch Star Wars with my daughter")
#Done
