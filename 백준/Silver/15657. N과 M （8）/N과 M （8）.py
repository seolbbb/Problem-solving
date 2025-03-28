def backtrack(num):
    if num == m:
        print(*seq)
        return
    
    for i in range(n):
        if seq and lst[i] < seq[-1]:
            continue
        seq.append(lst[i])
        backtrack(num+1)
        seq.pop()

n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
seq = []

backtrack(0)