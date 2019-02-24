# problem number 11727
import sys
first = True
case_number = 1
for line in sys.stdin:
    line = line.strip()
    if first:
        first = False
        continue
    if not first:
        line = line.split(" ")
        costs = sorted([int(x) for x in line])
        print("Case %s: %s" %(case_number, costs[1]))
        case_number += 1
