t_p = 1
p   = 1
for i in range(1, min(100, int(input()) + 1)):
    p *= i
    t_p = t_p + (-1.)**(i + 1) / p
print(t_p - 1)
