# import heapq
# import sys
# from functools import reduce
# #https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
# #heapify(list) => heap data structure representation
# #heappush(heap,ele)
# #heappop(heap)
#
# # take all numbers
# # heapify
# # add the 2 values and then rehapify
# lines = sys.stdin.readlines()
# low1 = 0
# low2 = 0
# for line_num in range(len(lines)):
#     if line_num % 2 == 0:
#         continue
#     else:
#         og_values = list(map(int, lines[line_num].split()))
#         print(og_values)
#         cost = []
#         i = 0
#         intermediate_cost = 0
#         heapq.heapify(og_values)
#         while len(og_values) > 1:
#             intermediate_cost = 0
#             low1 = heapq.heappop(og_values)
#             # print(og_values)
#             low2 = heapq.heappop(og_values)
#             # print(og_values)
#             # print("--------")
#             intermediate_cost += low1 + low2
#             cost.append(intermediate_cost)
#             heapq.heappush(og_values, intermediate_cost)
#             print(og_values)
#             # print("--------")
#         # print("ANSWER")
#         print(reduce((lambda x, y: x + y), cost))
 

import heapq
import sys
from functools import reduce
lines = sys.stdin.readlines()
low1 = 0
low2 = 0
for line_num in range(len(lines)):
    if line_num % 2 == 0:
        continue
    else:
        og_values = list(map(int, lines[line_num].split()))
        cost = 0
        intermediate_cost = 0
        heapq.heapify(og_values)
        while len(og_values) > 1:
            intermediate_cost = 0
            low1 = heapq.heappop(og_values)
            low2 = heapq.heappop(og_values)
            intermediate_cost += low1 + low2
            cost += intermediate_cost
            heapq.heappush(og_values, intermediate_cost)
        print(cost)
