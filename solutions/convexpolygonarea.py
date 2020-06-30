#https://open.kattis.com/problems/convexpolygonarea
#https://en.wikipedia.org/wiki/Shoelace_formula

from geometry import convex_polygon_area

"""
def convex_polygon_area(tuple_list):
  x = tuple_list
  A = 0
  n = len(x)
  for i in range(n):
    A += (x[i%n][0]*x[(i+1)%n][1] - x[(i+1)%n][0]*x[i%n][1])
  return abs(A/2)
"""


if __name__ == "__main__":
  cases_n = int(input())
  for _ in range(cases_n):
    inp = list(map(int,input().split()))[1:]
    tuples = [(inp[i], inp[i+1]) for i in range(0,len(inp),2)]
    print(convex_polygon_area(tuples))
