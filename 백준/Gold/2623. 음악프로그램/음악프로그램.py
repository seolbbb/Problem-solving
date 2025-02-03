from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
in_order = [0 for _ in range(n+1)]
ans = []

for _ in range(m):
    seq = list(map(int, input().split()))
    k = seq[0]
    for i in range(1, k):
        graph[seq[i]].append(seq[i+1])
        in_order[seq[i+1]] += 1

queue = deque()
for i in range(1, n+1):
    if in_order[i] == 0:
        queue.append(i)

while queue:
    cur = queue.popleft()
    ans.append(cur)

    for nxt in graph[cur]:
        in_order[nxt] -= 1
        if in_order[nxt] == 0:
            queue.append(nxt)
    
if len(ans) == n:
    for name in ans:
        print(name)
else:
    print(0)