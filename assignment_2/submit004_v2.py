from collections import defaultdict

# import os
# cwd = os.getcwd()  # Get the current working directory (cwd)
# filename = cwd + "/33609_reads.txt"
# with open(filename, 'r') as fobj:
#     all_lines = fobj.read().splitlines()

# default_read = int(input("Enter number of reads: "))
# a = set()
# from random import randint
# while len(a) < default_read:
#     a.add(randint(0, 33608))

# reads_list = []
# for i in a:
#     k = randint(0, 89)
#     reads_list.append(all_lines[i][k:k+10])

# reads_list = sorted(reads_list)

default_read = int(input("Enter number of k-mers: "))
reads_list = []
for _ in range(default_read):
    reads_list.append(input("Enter k-mer: "))

adj = defaultdict(list)
id = 0
for read in reads_list:
    adj[read[:-1]].append((read[1:],id))
    id += 1

path = [reads_list[0][:-1]]
already_visited = set()

while len(already_visited) < len(reads_list):
    for i, node in enumerate(path):
        allVisited = True
        for next in adj[node]:
            if next[1] not in already_visited:
                allVisited = False
                break
        if allVisited: continue
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
        break
    path = path[:i]+new_cycle+path[i+1:]
cycle = ""

for node in path:
    cycle += node[0]
print("ASSEMBELED GENOME: " + cycle[:-1] + '\n')