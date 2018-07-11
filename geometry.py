def convex_polygon_area(tuple_list):
  x = tuple_list
  A = 0
  n = len(x)
  for i in range(n):
    A += (x[i%n][0]*x[(i+1)%n][1] - x[(i+1)%n][0]*x[i%n][1])
  return abs(A/2)
