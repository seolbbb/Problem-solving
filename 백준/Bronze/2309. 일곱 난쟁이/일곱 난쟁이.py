smurf = []
ans = []

for _ in range(9):
    smurf.append(int(input()))
smurf.sort()

for i in range(8):
    for j in range(i+1, 9):
        h = sum(smurf)
        a = smurf[i]
        b = smurf[j]
        h -= (a + b)

        if h == 100:
            smurf.remove(a)
            smurf.remove(b)
            print(*smurf, sep='\n')
            exit()