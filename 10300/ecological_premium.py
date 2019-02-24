import sys

lines = sys.stdin.readlines()
i = 1                             # skip first line
while i < len(lines):
    farmers = int(lines[i])       # number of farmers in this case
    i += 1                        # after reading, go to next line
    cost = 0
    for _ in range(farmers):
        footage, animals, friendliness = [int(x) for x in lines[i].split(' ')]
        cost += footage * friendliness
        i += 1                    # go to next line
    print(cost)
