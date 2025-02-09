from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    h, w = map(int, input().split())

    original_board = [list(input().strip()) for _ in range(h)]
    keys_str = input().strip()
    key = 0
    if keys_str != "0":
        for k in keys_str:
            key |= (1 << (ord(k) - ord('a')))

    H = h + 2
    W = w + 2
    board = [['.' for _ in range(W)] for _ in range(H)]
    for i in range(h):
        for j in range(w):
            board[i + 1][j + 1] = original_board[i][j]

    waiting_doors = {chr(c): [] for c in range(ord('A'), ord('Z') + 1)}

    ans = 0
    queue = deque()
    queue.append((0, 0))
    visited = [[False] * W for _ in range(H)]
    visited[0][0] = True

    # (0,0)부터 시작하는 BFS 탐색
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if visited[nx][ny] or board[nx][ny] == '*':
                continue

            cell = board[nx][ny]
            visited[nx][ny] = 1

            # 문서 발견 시
            if cell == '$':
                ans += 1
                board[nx][ny] = '.'
                queue.append((nx, ny))

            # 열쇠 발견 시
            elif 'a' <= cell <= 'z':
                # 만약 지금까지 갖고 있지 않은 새 열쇠라면
                if not (key & (1 << (ord(cell) - ord('a')))):
                    key |= (1 << (ord(cell) - ord('a')))
                    # 대기 중인 문들 중 이 열쇠로 열 수 있는 문 큐에 추가
                    door_char = cell.upper()
                    for door_pos in waiting_doors[door_char]:
                        queue.append(door_pos)
                    waiting_doors[door_char] = []
                board[nx][ny] = '.' 
                queue.append((nx, ny))

            # 문 발견 시
            elif 'A' <= cell <= 'Z':
                # 현재 소지한 열쇠로 열 수 있다면
                if key & (1 << (ord(cell) - ord('A'))):
                    board[nx][ny] = '.'  # 문을 열고
                    queue.append((nx, ny))
                else:
                    # 대기 중인 문에 추가
                    waiting_doors[cell].append((nx, ny))
            else:
                # 빈 공간이면 그냥 이동
                queue.append((nx, ny))

    print(ans)