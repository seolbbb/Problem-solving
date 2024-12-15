m = int(input())
n = int(input())

primes = []

x = [i for i in range(m,n+1) if i != 1]

out = 0

for i in x:
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            out = 1
            break
    if out == 0:
        primes.append(i)
    out = 0

if len(primes) != 0:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)