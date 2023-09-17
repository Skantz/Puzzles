def babylonian_sqrt(S):
    if S == 0:
        return 0
    x = S/2
    for _ in range(20):
        x = 0.5 * (x + S/x)
    return x
