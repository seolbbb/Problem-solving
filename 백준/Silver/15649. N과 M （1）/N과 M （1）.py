def back_track(length):
    if length == m:
        print(*arr)
        return
    
    for idx in range(1,n+1):
        if not visited[idx]:
            arr.append(idx)
            visited[idx] = True
            back_track(length+1)
            arr.pop()
            visited[idx] = False


n,m = map(int,input().split())
arr = []
nums = [i+1 for i in range(n+1)]
visited = [False] * (n+1)
back_track(0)