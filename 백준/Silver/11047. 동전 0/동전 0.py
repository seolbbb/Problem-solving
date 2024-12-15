n, k = map(int,input().split())
n_lst = []

for i in range(n):
    n_lst.append(int(input()))

cnt = 0
i = n-1

while k:
    if n_lst[i] > k:
        i -= 1
    else:
        cnt += k // n_lst[i]
        k = k % n_lst[i]

print(cnt)