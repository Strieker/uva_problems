# problem number 11764
import sys
lines = sys.stdin.readlines()
first = True
line_counter = 0
total_cases = 0
case_number = 0
line = lines[0]
if first:
    line_counter += 1
    total_cases = int(line)
    first = False
while line_counter != len(lines):
    line = lines[line_counter]
    if line_counter % 2 == 0:
        line = line.replace("\n","")
        total_low_jumps = 0
        total_high_jumps = 0
        i = 0
        j = 1
        jumps = [int(x) for x in line.split(" ")]
        if len(jumps) == 1:
            total_high_jumps = 0
            total_low_jumps = 0
        else:
            length = len(jumps)
            for i in range(0, length - 1):
                if jumps[i] > jumps[j]:
                    total_low_jumps += 1
                elif jumps[i] < jumps[j]:
                    total_high_jumps += 1
                j += 1
        case_number += 1
        print("Case %s: %s %s" %(case_number, total_high_jumps, total_low_jumps))

    line_counter += 1
