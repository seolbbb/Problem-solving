import sys

n, m = map(int,sys.stdin.readline().split())
pokemon = {}

for i in range(n):
    pokemon[sys.stdin.readline().rstrip()] = i

pokemon2 = {v:k for k,v in pokemon.items()}

for i in range(m):
    x = sys.stdin.readline().rstrip()

    if x.isalpha():
        print(pokemon[x]+1)
    else:
        print(pokemon2[int(x)-1])