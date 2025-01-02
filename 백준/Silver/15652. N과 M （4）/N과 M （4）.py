def backtrack(start):
    if len(s) == m:
        print(' '.join(map(str,s)))
        return   
    for i in range(start-1,n+1):
            if i == 0:
                 continue
            s.append(i)
            backtrack(i+1)
            s.pop()

n,m = map(int,input().split())
s = []
backtrack(1)