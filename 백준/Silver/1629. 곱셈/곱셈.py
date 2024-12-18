def pow(a,b,c):
    if b == 1:
        return a % c
    
    val = pow(a,b//2,c)
    if b % 2 == 0:
        return val*val%c
    else:
        return val*val*a%c


a,b,c = map(int,input().split())

print(pow(a,b,c))