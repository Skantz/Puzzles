#https://open.kattis.com/problems/4thought
n = int(input())
operators = ["+", "-", "*", "//"]
calculations  = ["4 " + x_op + " 4 " + y_op + " 4 " + z_op + " 4" for x_op in operators for y_op in operators for z_op in operators]
targets = []
_ = [exec("targets.append(" + c + ")") for c in calculations]
for _ in range(n):
    goal = int(input())
    if goal in targets:
        idx = targets.index(goal)
        print(calculations[idx].replace("//", "/") + " = " + str(goal))
    else:
        print("no solution")
#Done
