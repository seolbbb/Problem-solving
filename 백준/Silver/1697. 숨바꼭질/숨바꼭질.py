from collections import deque

n, k = map(int, input().split())

time = [-1 for _ in range(100001)]
queue = deque([n])
time[n] = 0

while queue:
    cur = queue.popleft()
    move = (cur - 1, cur + 1, cur * 2)

    for nxt in move:
        if nxt < 0 or nxt > 100000:
            continue
        if time[nxt] == -1:
            time[nxt] = time[cur] + 1
            queue.append(nxt)

print(time[k])