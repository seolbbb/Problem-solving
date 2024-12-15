n = int(input())
x = list(map(int, input().split()))
t, p = map(int, input().split())

shirt = 0
pen = 0
pen2 = 0

for i in range(6):
    if x[i] == 0:
        pass
    elif x[i] - t <= 0:
        shirt += 1
    elif x[i] % t == 0:
        shirt += ((x[i] // t))
    else:
        shirt += ((x[i] // t) + 1)

pen, pen2 = divmod(n,p)

print(shirt)
print(pen, end=' ')
print(pen2, end='')