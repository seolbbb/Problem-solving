n = 1000 - int(input())
change = [500,100,50,10,5,1]
i = 0
res = 0

while n:
    if n // change[i] >= 1:
        res += n // change[i]
        n %= change[i]
        i += 1
    else:
        i += 1

print(res)