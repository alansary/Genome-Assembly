from collections import defaultdict

default_read = int(input("Enter number of reads: "))

reads_list = []
for _ in range(default_read):
    reads_list.append(input())

adj = defaultdict(list)
id = 0
for read in reads_list:
    adj[read[:-1]].append((read[1:],id))
    id += 1

path = [reads_list[0][:-1]]
already_visited = set()

# # x = 1
# while len(already_visited) < len(reads_list):
#     # y = 1
#     # print (x)
#     for i, node in enumerate(path):
#         # z = 1
#         # print (x, y)
#         allVisited = True
#         for next in adj[node]:
#             # print (x, y, 1, z)
#             if next[1] not in already_visited:
#                 allVisited = False
#                 break
#             # z += 1
#         if allVisited: continue
#         new_cycle = [node]
#         current = node
#         find_Next = True
#         # z = 1
#         while find_Next:
#             # w = 1
#             # print (x, y, 2, z)
#             find_Next = False
#             for next in adj[current]:
#                 # print (x, y, 2, z, w)
#                 if next[1] not in already_visited:
#                     already_visited.add(next[1])
#                     new_cycle.append(next[0])
#                     current = next[0]
#                     find_Next = True
#                     break
#                 # w += 1
#             # z += 1
#         # y += 1
#         break
#     path = path[:i]+new_cycle+path[i+1:]
#     # x += 1

i = 0
node = path[i]
new_cycle = [node]
current = node
find_Next = True
while find_Next:
    find_Next = False
    for next in adj[current]:
        if next[1] not in already_visited:
            already_visited.add(next[1])
            new_cycle.append(next[0])
            current = next[0]
            find_Next = True
            break

path = path[:i]+new_cycle+path[i+1:]
cycle = ""

for node in path:
    cycle += node[0]
print(cycle[:-1])