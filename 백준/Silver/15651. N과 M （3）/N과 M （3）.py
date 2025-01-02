def backtrack():
    if len(s) == m:
        print(' '.join(map(str,s)))
        return   
    for i in range(1,n+1):
            s.append(i)
            backtrack()
            s.pop()

n,m = map(int,input().split())
s = []
backtrack()