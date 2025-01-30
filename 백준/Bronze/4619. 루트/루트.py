while True:
    b, n = map(int, input().split())
    ans = 0

    if b == 0 and n == 0:
        break
        
    a = int((b**(1/n)))
    
    if abs(b-a**n) > abs(b-(a+1)**n):
        print(a+1)
    else:
        print(a)