import sys

while True:
    try:
        size, num_queries = map(int, sys.stdin.readline().split())
        to_query = list(map(int, sys.stdin.readline().split()))

        g = {}
        #sparse dictionary
        for i, x in enumerate(to_query):
            if x not in g:
                g[x] = []
            g[x].append(i+1)
        for _ in range(num_queries):
            k,v = map(int, sys.stdin.readline().split())
            if len(g[v]) < k:
                print(0)
            else:
                print(g[v][k-1])
    except:
        break
