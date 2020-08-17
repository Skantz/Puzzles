n = int(input())

while n > 9:
    n_ = 1
    for _, v in enumerate(str(n)):
        n_ *= max(1, int(v))
    n = n_
print(n)
