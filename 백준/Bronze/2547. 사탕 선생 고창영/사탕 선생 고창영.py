t = int(input())

for _ in range(t):
    candy = 0
    m = input()
    n = int(input())
    for _ in range(n):
        i = int(input())
        candy += i
    
    if candy % n == 0:
        print('YES')
    else:
        print('NO')