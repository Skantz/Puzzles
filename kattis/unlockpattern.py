#We would like the distance between two points in a (square) "unit matrix"

n = 9   # amount of elements

r = int(n**0.5) #amount of elements on a row

#We would like a row and column distance between two points

def point_distance(p_1, p_2, n):  #-1 because of 0-indices
  r = int(n**0.5)
  x_dist = abs((p_1-1) % r - (p_2-1) % r)
  y_dist = abs((p_1-1) // r - (p_2-1) // r)
  return (x_dist ** 2 + y_dist ** 2)**0.5

def path_distance(path_list, n):
  p = path_list
  return sum([point_distance(p[i],p[i+1],n) for i in range(n-1)])

#print(path_distance([2,5,8,7,4,1,5,9,6,3],9))

def solve_3x3():
  path_list = []
  inp_list  = []
  for _ in range(3):
    inp_list += list(map(int,input().split()))
  for i in range(1,10):
    path_list.append(inp_list.index(i)+1)
  return path_distance(path_list,9)

print(solve_3x3())
