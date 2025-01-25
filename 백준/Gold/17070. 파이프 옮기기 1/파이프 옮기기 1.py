import sys
input = input
sys.setrecursionlimit(10**7)

def dfs(r, c, d):
    if memo[r][c][d] != -1:
        return memo[r][c][d]
    
    if r == n - 1 and c == n - 1:
        return 1
    
    ways = 0
    
    # 1) 가로 방향 이동이 가능한지 체크
    if d == 0 or d == 1:
        nr, nc = r, c + 1
        if nc < n and board[nr][nc] == 0:
            ways += dfs(nr, nc, 0)
        
    # 2) 세로 방향 이동이 가능한지 체크
    if d == 2 or d == 1:
        nr, nc = r + 1, c
        if nr < n and board[nr][nc] == 0:
            ways += dfs(nr, nc, 2)

    # 3) 대각선 이동
    nr, nc = r + 1, c + 1
    if nr < n and nc < n:
        if board[r][c+1] == 0 and board[r+1][c] == 0 and board[nr][nc] == 0:
            ways += dfs(nr, nc, 1)
    
    memo[r][c][d] = ways
    return ways


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
memo = [[[-1, -1, -1] for _ in range(n)] for _ in range(n)]

print(dfs(0, 1, 0))