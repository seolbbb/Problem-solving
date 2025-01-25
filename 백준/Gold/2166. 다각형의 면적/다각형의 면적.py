n = int(input())
x = []
y = []
ans = 0

for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
x.append(x[0])
y.append(y[0])

for i in range(n):
    ans += x[i] * y[i+1]
    ans -= y[i] * x[i+1]

print(abs(ans)/2)