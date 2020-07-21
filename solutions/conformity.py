#https://open.kattis.com/problems/conformity
n = int(input().strip())
choice = {}
for _ in range(n):
    inp = input().strip()
    inp = [int(e) for e in inp.split(" ")]
    inp.sort()
    inp = " ".join([str(e) for e in inp])
    try:
        choice[inp] += 1
    except:
        choice[inp] = 1

m = max(choice.values())
print(m * list(choice.values()).count(m))
#Done
