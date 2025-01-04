import sys
input = sys.stdin.readline

def paper(r,c,m):
    global cnt1, cnt2, cnt3
    cur = arr[r][c]
    for i in range(r,r+m):
        for j in range(c,c+m):
            if arr[i][j] != cur:
                for k in range(3):
                    for l in range(3):
                        paper(r+k*(m//3),c+l*(m//3),m//3)
                return

    if cur == -1:
        cnt1 += 1
    elif cur == 0:
        cnt2 += 1
    else:
        cnt3 += 1

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
cnt1 = 0
cnt2 = 0
cnt3 = 0

paper(0,0,n)
print(cnt1)
print(cnt2)
print(cnt3)