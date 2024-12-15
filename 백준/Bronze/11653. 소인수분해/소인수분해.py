n = int(input())

primes = []
factors = []

if n == 1:
    exit(0)
else:
    for i in range(2, int(n**0.5)+1):
        prime = 1
        for j in range(2,i):
            if i%j == 0:
                prime = 0

        if prime == 1:
            primes.append(i)

    for prime in primes:
        while n % prime == 0:
            n //= prime
            print(prime)
    if n != 1:
        print(n)