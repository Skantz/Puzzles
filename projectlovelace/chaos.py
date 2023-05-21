def logistic_map(r):
    x = 0.5
    xs = [x]
    for _ in range(50):
        x = r * x * (1 - x)
        xs.append(x)
    return xs
