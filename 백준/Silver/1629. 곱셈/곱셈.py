def POW(a,b,c):
    if b == 1:
        return a % c
    val = POW(a,b//2,c)
    val = val * val % c
    if b % 2 == 0:
        return val
    else:
        return val * a % c    

a, b, c = map(int,input().split())

print(POW(a,b,c))