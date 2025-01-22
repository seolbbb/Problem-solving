t = int(input())
cnt = []

cnt.append(t//300)
t %= 300
cnt.append(t//60)
t %= 60
cnt.append(t//10)
t %= 10

if t:
    print(-1)
else:
    print(' '.join(map(str,cnt)))