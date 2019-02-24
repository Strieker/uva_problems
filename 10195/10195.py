import sys
import math
cases = sys.stdin.readlines()

for case in cases:
    x, y, z = map(float, case.strip().split())
    if x <= 0 or y <= 0 or z <= 0:
        r = 0.000
    else:
        p = x + y + z
        hp = p/2.0
        a = math.sqrt(hp * (hp -x) * (hp -y) * (hp - z))
        r = 2.0*a/p
    print("The radius of the round table is: {:.3f}".format(r))
