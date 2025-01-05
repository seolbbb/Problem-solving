import sys
input = sys.stdin.readline

def paper(r,c,m):
    global cnt1, cnt2
    cur = arr[r][c]
    for i in range(r,r+m):
        for j in range(c,c+m):
            if cur != arr[i][j]:
                for k in range(2):
                    for l in range(2):
                        paper(r+k*(m//2),c+l*(m//2),m//2)
                return
    
    if cur == 0:
        cnt1 += 1
    else:
        cnt2 += 1

n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
cnt1 = 0
cnt2 = 0

paper(0,0,n)

print(cnt1)
print(cnt2)