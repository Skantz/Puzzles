from sys import stdin
from math import factorial
from functools import reduce 
import operator


def anagram_count(string):
  characters = list(string)
  uniques = {}
  for c in characters:
    uniques[c] = 1
  factorial_of_counts = [factorial(characters.count(c)) for c in uniques.keys()]
  return factorial(len(string))//reduce(operator.mul, factorial_of_counts, 1)

for inp in stdin:
  print(anagram_count(inp.strip()))
