n, m = map(int ,input().split())
arr1 = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
arr2 = [list(map(int, input().split())) for _ in range(m)]

res = [[0 for _ in range(k)] for _ in range(n)]

for i in range(n):
    for j in range(k):
        s = 0
        for q in range(m):
            s += arr1[i][q]*arr2[q][j]
        res[i][j] = s

for row in res:
    print(*row)