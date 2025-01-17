n = int(input())

n_num = []
p_num = []
zero = 0
res = 0

for _ in range(n):
    m = int(input())
    if m == 0:
        zero = 1
    elif m == 1:
        res += 1
    elif m < 0:
        n_num.append(m)
    else:
        p_num.append(m)

n_num.sort()
p_num.sort(reverse = True)

for i in range(0, len(n_num)-1, 2):
    res += n_num[i] * n_num[i+1]

if len(n_num) % 2 == 1:
    if zero == 0:
        res += n_num[-1]

for i in range(0, len(p_num)-1, 2):
    res += p_num[i] * p_num[i+1]

if len(p_num) % 2 == 1:
    res += p_num[-1]

print(res)