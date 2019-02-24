#memorize the first three lines
import sys
import re
#purpse of first variable is to ignore the first input
first = True
for line in sys.stdin:
    line = line.strip()
    #good way to check
    if not first:
        #splits the input by a space
        x,y = re.split(r'\s+', line)
        x = int(x)
        y = int(y)
        if x < y:
            print('<')
        elif x > y:
            print('>')
        else:
            print('=')
    first = False
