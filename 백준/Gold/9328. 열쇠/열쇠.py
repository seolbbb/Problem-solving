'''
열쇠, 문 bitmask로 관리
1. 시작 가능 위치, 접근 가능한 문 check
2. 시작 가능 위치에서 bfs -> 접근 가능한 문, 얻은 열쇠, 얻은 문서 check
3. 현재 소지한 열쇠로 열 수 있는 문 열기
열 수 있는 문이 있으면 다시 1번으로
열 수 있는 문이 없다면 end
'''
from collections import deque

# 입구, 입구에 있는 문의 좌표 확인
def start_check():
    global key, ans
    start = []

    for i in range(h):
        for j in range(w):
            if i == 0 or i == h-1 or j == 0 or j == w-1:
                if board[i][j].islower():
                    bit = ord(board[i][j]) - ord('a')
                    key = key | (1 << bit)
                    board[i][j] = '.'
                if board[i][j].isupper():
                    bit = ord(board[i][j]) - ord('A')
                    doors.add(((1 << bit), i, j))
                if board[i][j] == '$':
                    ans += 1
                    board[i][j] = '.'
                if board[i][j] == '.':
                    start.append((i, j))
    return start

# 현재 소지한 열쇠로 열 수 있는 문 열기
def open_door():
    global doors
    end = 1
    remove = set()

    for door, r, c in doors:
        # door과 key의 비트마스크 and 연산을 통해 key를 가지고 있는지 확인
        if door & key:
            board[r][c] = '.'
            remove.add((door, r, c))
            end = 0

    #문이 하나도 안 열렸으면 1 반환
    if end == 1:
        return 1
    else:
        doors = doors - remove
        return 0

# bfs 탐색
def bfs(row, col):
    global ans, key

    visit = [[0 for _ in range(w)] for _ in range(h)]
    queue = deque([(row, col)])
    visit[row][col] = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if visit[nx][ny] == 1 or board[nx][ny] == '*':
                continue
            # 문 발견 시 doors에 비트마스크 추가
            if board[nx][ny].isupper():
                bit = ord(board[nx][ny]) - ord('A')
                doors.add(((1 << bit), nx, ny))
                continue
            # 열쇠 발견 시 key와 or 연산으로 비트마스크에 추가
            if board[nx][ny].islower():
                bit = ord(board[nx][ny]) - ord('a')
                key = key | (1 << bit)
                board[nx][ny] = '.'

            if board[nx][ny] == '$':
                ans += 1
                board[nx][ny] = '.'

            queue.append((nx, ny))
            visit[nx][ny] = 1

t = int(input())

for _ in range(t):
    h, w = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    tmp_key = list(input())
    key = 0

    if tmp_key[0] != '0':
        for k in tmp_key:
            bit = ord(k) - ord('a')
            key = key | (1 << bit)

    doors = set()
    ans = 0

    # 건물 입구가 문으로 막혀 있는 경우 check
    # start_check()와 open_door() 한 번 실행
    start_check()
    open_door()
    start = start_check()

    # 건물에 들어갈 수 없으면 0 출력
    if not start:
        print(0)
        continue

    while True:
        for row, col in start:
            bfs(row, col)
        end = open_door()

        # print(*board, sep= '\n')
        # print(ans)
        # print()

        # 아무 문도 열 수 없으면 end
        if end == 1:
            break
        start = start_check()
    
    print(ans)