def hail(x):
    if x == 1:
        return x
    elif not (x % 2):
        return x + hail(x//2)
    else:
        return x + hail(3*x + 1)
print(hail(int(input())))
