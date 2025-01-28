arr = [[0,1,1,0,0,0,0,0],
       [1,0,1,1,0,0,0,0],
       [1,1,0,1,1,0,0,0],
       [0,1,1,0,1,1,0,0],
       [0,0,1,1,0,1,0,1],
       [0,0,0,1,1,0,1,0],
       [0,0,0,0,0,1,0,1],
       [0,0,0,0,1,0,1,0]]

def matmul(a, b):
    c = [[0 for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            s = 0
            for k in range(8):
                s += a[i][k]*b[k][j]
            c[i][j] = s % 1000000007
    return c

def matpow(m, exp):
    result = [[0 for _ in range(8)] for _ in range(8)]
    for i in range(8):
        result[i][i] = 1
    
    base = m
    e = exp

    while e > 0:
        if e & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        e //= 2
    return result

d = int(input())

ans = matpow(arr, d)[0][0] % 1000000007
print(ans)