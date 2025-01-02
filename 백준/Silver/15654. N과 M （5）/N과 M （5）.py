def backtrack():
    if len(arr) == m:
        print(' '.join(map(str,arr)))
        return   
    for i in range(n):
        if s[i] not in arr:
            arr.append(s[i])
            backtrack()
            arr.pop()

n,m = map(int,input().split())
s = list(map(int,input().split()))
s.sort()
arr = []
backtrack()