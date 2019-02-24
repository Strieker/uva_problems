import sys

# Nodes are triples [data, parent, size]



class Disjoint_Set():
    def __init__(self):
        self.network = {}
    def add(self, x):
        if x not in self.network:
            self.network[x] = [x, None, 1]
    def union(self, x, y): # return the size of the new group
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return x_root[2]
        if x_root[2] < y_root[2]:
            x_root, y_root = y_root, x_root
        y_root[1] = x_root[0]
        x_root[2] += y_root[2]
        return x_root[2]
    def find(self, x):
        if self.network[x][1] is not None:
            self.network[x] = self.find(self.network[x][1])
        return self.network[x]

cases = int(sys.stdin.readline())
blank = sys.stdin.readline()

for _ in range(cases):
    if _ != 0:
        print()
    num_computers = int(sys.stdin.readline())
    network = Disjoint_Set()
    for c in range(1, num_computers + 1):
        network.add(c)
    found = 0
    not_found = 0
    while True:
        try:
            letter, computer1, computer2 = sys.stdin.readline().split()
            computer1 = int(computer1)
            computer2 = int(computer2)
            if letter == 'c':
                network.union(computer1,computer2)
            elif letter == "q":
                computer1connection = network.find(computer1)
                computer2connection = network.find(computer2)
                if computer1connection != computer2connection:
                    not_found += 1
                else:
                    found += 1
        except:
            break
    print("%s,%s"%(found,not_found))
