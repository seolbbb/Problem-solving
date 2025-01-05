def queen(row_idx):
    global cnt
    if row_idx == n:
        cnt += 1
        return
    for col_idx in range(n):
        if col[col_idx] == 1 or diag1[row_idx+col_idx] == 1 or diag2[row_idx-col_idx + (n-1)] == 1:
            continue
        col[col_idx] = 1
        diag1[row_idx+col_idx] = 1
        diag2[row_idx-col_idx + (n-1)] = 1
        queen(row_idx+1)
        col[col_idx] = 0
        diag1[row_idx+col_idx] = 0
        diag2[row_idx-col_idx + (n-1)] = 0

n = int(input())
cnt = 0
lst1 = []
lst2 = []
col = [0 for _ in range(n)]
diag1 = [0 for _ in range(2*n - 1)]
diag2 = [0 for _ in range(2*n - 1)]

queen(0)
print(cnt)