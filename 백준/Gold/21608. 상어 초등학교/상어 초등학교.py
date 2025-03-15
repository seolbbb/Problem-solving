import sys
input = sys.stdin.readline

n = int(input())
board = [[0 for _ in range(n+1)] for _ in range(n+1)]
fr = dict()
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ans = 0

for _ in range(n**2):
    lst = list(map(int, input().split()))
    cor = [[[] for _ in range(5)] for _ in range(5)]
    cur_student = lst[0]
    friend = set(lst[1:])
    fr[cur_student] = friend

    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][j] != 0:
                continue
            adj_cnt = 0
            empty_cnt = 0

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if nx < 1 or nx > n or ny < 1 or ny > n:
                    continue
                if board[nx][ny] == 0:
                    empty_cnt += 1
                elif board[nx][ny] in friend:
                    adj_cnt += 1
                
            cor[adj_cnt][empty_cnt].append((i, j))
            Break = 0

    for p in range(4, -1, -1):
        if Break:
            break
        for q in range(4, -1, -1):
            cor_lst = cor[p][q]
            if cor_lst:
                cor_lst.sort(key=lambda x: (x[0], x[1]))
                x, y = cor_lst[0]
                board[x][y] = cur_student
                Break = 1
            if Break:
                break

for i in range(1, n+1):
    for j in range(1, n+1):
        adj_cnt = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if nx < 1 or nx > n or ny < 1 or ny > n:
                continue
            if board[nx][ny] in fr[board[i][j]]:
                adj_cnt += 1

        if adj_cnt > 0:
            ans += 10**(adj_cnt - 1)

print(ans)