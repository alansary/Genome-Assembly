from collections import defaultdict

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
print("ASSEMBELED GENOME: " + cycle[:-1] + '\n')