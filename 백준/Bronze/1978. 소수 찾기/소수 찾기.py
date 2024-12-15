n = int(input())

x = list(map(int,input().split()))

x = [i for i in x if i != 1]

for i in range(len(x)):
    a = x[i]

    for j in range(2, a):
        if a % j == 0:
            x[i] = 0
            break

print(len([n for n in x if n != 0]))