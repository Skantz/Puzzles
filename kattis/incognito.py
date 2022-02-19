import sys

sys.stdin.readline()
for i in sys.stdin:
  outfits = {}
  for j in range(0,int(i)):
    line = sys.stdin.readline().split()
    if line[1] in outfits:
      outfits[line[1]].add(line[0])
    else:
      outfits[line[1]]={line[0]}
  count = 1
  for i in outfits:
    count *= len(outfits[i])+1
  print(count-1)
