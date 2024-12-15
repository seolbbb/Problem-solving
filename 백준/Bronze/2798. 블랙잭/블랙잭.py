n, m = map(int,input().split())
x = list(map(int,input().split()))
v = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            a = x[i] + x[j] + x[k]
            if (a <= m)and(a > v): # a
                v = a

print(v)