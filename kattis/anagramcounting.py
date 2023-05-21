from sys import stdin
from math import factorial
from functools import reduce 
import operator

def anagram_count(string):
  characters = list(string)
  uniques = {c: 1 for c in characters}
  factorial_of_counts = [factorial(characters.count(c)) for c in uniques.keys()]
  return factorial(len(string))//reduce(operator.mul, factorial_of_counts, 1)

for inp in stdin:
  print(anagram_count(inp.strip()))
