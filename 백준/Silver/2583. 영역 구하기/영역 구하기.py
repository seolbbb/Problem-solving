import sys
from collections import deque
input = sys.stdin.readline

m, n, k = map(int, input().split())
board = [[0 for _ in range(n)] for _ in range(m)]
visit = [[0 for _ in range(n)] for _ in range(m)]
queue = deque()
ans = []

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            board[j][i] = 1

for i in range(m):
    for j in range(n):
        if visit[i][j] == 1 or board[i][j] == 1:
            continue
        
        cnt = 1
        queue.append((i, j))
        visit[i][j] = 1

        while queue:
            x, y = queue.popleft()

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nx = x + dx
                ny = y + dy

                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if visit[nx][ny] == 1 or board[nx][ny] == 1:
                    continue
                
                queue.append((nx, ny))
                visit[nx][ny] = 1
                cnt += 1
        
        ans.append(cnt)

ans.sort()

print(len(ans))
print(*ans)