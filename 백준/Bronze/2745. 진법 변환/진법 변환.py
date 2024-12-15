n, b = input().split()
b = int(b)
ans = 0
x = 0

for i in range(len(n)):
    try:
        x = int(n[i])
        ans += x * (b ** (len(n)-1-i))
    except ValueError:
        x = ord(n[i]) - 55
        ans += x * (b ** (len(n)-1-i))

print(ans)