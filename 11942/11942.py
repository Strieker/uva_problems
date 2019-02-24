import sys
# regular expression 
import re
first = True
for line in sys.stdin:
    line = line.strip()
    if first:
        print('Lumberjacks:')
    else:
        a = re.split(r'\s+', line)
        a = [int(x) for x in a]
        if a == sorted(a) or a == sorted(a, reverse = True):
            print('Ordered')
        else:
            print('Unordered')
    first = False
