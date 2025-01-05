import sys
input = sys.stdin.readline

def quadtree(r,c,m):
    global result
    cur = arr[r][c]
    for i in range(r,r+m):
        for j in range(c,c+m):
            if cur != arr[i][j]:
                result += "("
                for k in range(2):
                    for l in range(2):
                        quadtree(r+k*(m//2),c+l*(m//2),m//2)
                result += ")"
                return
    if cur == 1:
        result += "1"
    else:
        result += "0"



n = int(input())
arr = [list(map(int,input().rstrip())) for _ in range(n)]
result = ""

quadtree(0,0,n)
print(result)