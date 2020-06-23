import re

cases_n = int(input())

name_converter = lambda name: 2 if name == "upper" else (1 if name == "middle"
                                else (0 if name == "lower" else name))

radix = 0

def read_and_convert():
  people_n = int(input())
  list_of_people_and_class = []
  for _ in range(people_n):
#    list_of_people_and_class.append(re.sub([" "],"",re.split(':|-',input())))
    list_of_people_and_class.append(re.split(':|-',re.sub('class| ',"",input())))
  radix = max([len(t) for t in list_of_people_and_class[1]]) - 1
  return [(pc[0],[name_converter(c) for c in pc[1:]]) for pc in list_of_people_and_class]

print(read_and_convert())

def sort_name_class_tuples(name_class_tuples):
  pass
