s = int(input())
n = 1
total = 1

while True:
    if n % 2 == 1:
        total = ((1+n)*(n//2))+((n+1)//2)
    else:
        total = (1+n)*(n//2)

    if total > s:
        n -= 1
        break
    elif total == s:
        break
    else:
        n += 1

print(n)