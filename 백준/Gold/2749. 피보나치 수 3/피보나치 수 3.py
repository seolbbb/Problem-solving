def matmul(a, base):
    m = len(a)
    c = [[0 for _ in range(m)] for _ in range(m)]
    
    for i in range(m):
        for j in range(m):
            s = 0
            for k in range(m):
                s += a[i][k]*base[k][j]
            c[i][j] = s % 1000000
    return c

def matpow(base, e):
    L = len(base)
    result = [[0 for _ in range(L)] for _ in range(L)]
    for i in range(L):
        result[i][i] = 1
    
    while e > 0:
        if e & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        e //= 2

    return result

n = int(input())
fib = [[1,1], [1,0]]
ans = matpow(fib, n)[1][0]
print(ans)