import sys
for i in range(int(sys.stdin.readline().strip())):
    #strip() kills the newline character
    val = (int(sys.stdin.readline().strip()))
    val = val * 567
    val = val // 9
    val = val + 7492
    val = val * 235
    val = val // 47
    val = val - 498
    val = abs(val)
    val = val // 10
    val = val % 10
    print(val)
