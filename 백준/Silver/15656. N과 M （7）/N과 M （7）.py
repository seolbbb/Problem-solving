def backtrack(num):
    if num == m:
        print(*ans)
        return
    
    for i in range(n):
        ans.append(lst[i])
        backtrack(num+1)
        ans.pop()

n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
ans = []

backtrack(0)