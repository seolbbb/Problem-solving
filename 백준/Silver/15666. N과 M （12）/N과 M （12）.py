import sys
input = sys.stdin.readline

def backtrack():
    if len(result) == m:
        if tuple(result) not in printed:
            print(" ".join(map(str,result)))
            printed[tuple(result)] = 1
            return
        else:
            return
    for i in range(n):
        if len(result) == 0 or arr[i] >= result[-1]:
            result.append(arr[i])
            backtrack()
            result.pop()


n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
printed = {}
result = []

backtrack()