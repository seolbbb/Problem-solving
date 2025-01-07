def backtrack(num):
    if num == m:
        print(" ".join(map(str,lst)))
        return
    for i in range(num,n):
        if num == 0 or arr[i] > lst[-1]:
            lst.append(arr[i])
            backtrack(num+1)
            lst.pop()


n,m = map(int,input().split())
arr = list(map(int,input().split()))
lst = []
arr.sort()

backtrack(0)