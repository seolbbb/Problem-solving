def backtrack():
    if len(arr) == m:
        if tuple(arr) not in printed:
            printed[tuple(arr)] = 1
            print(' '.join(map(str,arr)))
            return
        else:
            return

    for i in range(n):
        if i not in arr2:
            arr.append(s[i])
            arr2.append(i)
            backtrack()
            arr.pop()
            arr2.pop()

n,m = map(int,input().split())
s = list(map(int,input().split()))
s.sort()
arr = []
arr2 = []
printed = {}
backtrack()