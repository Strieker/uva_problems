import sys
import re
first = True
case_number = 0
for line in sys.stdin:
    line = line.strip()
    if not first:
        line = line.split(" ", 1)
        speeds = line[1].split(" ")
        speeds = [int(x) for x in speeds]
        print("Case %s: %s" %(case_number, max(speeds)))
    case_number = case_number + 1
    first = False
