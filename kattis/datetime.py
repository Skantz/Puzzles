import datetime

d, m = [int(x) for x in input().strip().split()]
 
date = datetime.date(2009, m, d)
print(date.strftime("%A"))
