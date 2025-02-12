import sys
input = sys.stdin.readline

n, m = map(int, input().split())

a = [list(map(int, list(input().rstrip()))) for _ in range(n)]
b = [list(map(int, list(input().rstrip()))) for _ in range(n)]
cnt = 0
diff = []

for i in range(n-2):
    for j in range(m-2):
        diff.append((i, j))

for x, y in diff:
    if a[x][y] != b[x][y]:
        cnt += 1
        for i in range(3):
            for j in range(3):
                a[x+i][j+y] = 1-a[x+i][j+y]

if a != b:
    cnt = -1

print(cnt)