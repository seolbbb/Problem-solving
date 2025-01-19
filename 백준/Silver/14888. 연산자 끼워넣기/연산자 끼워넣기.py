def insert_op():
    if len(lst) == n-1 and tuple(lst) not in used2:
        used2[tuple(lst)] = 1
        m = arr[0]

        for i in range(n-1):
            if lst[i] == '+':
                m = m + arr[i+1]
            elif lst[i] == '-':
                m = m - arr[i+1]
            elif lst[i] == '*':
                m = m * arr[i+1]
            else:
                if m < 0:
                    m = -(-m // arr[i+1])
                else:
                    m = m // arr[i+1]
        res.append(m)

    for i in range(n-1):
        if used[i] == 1:
            continue
        lst.append(op2[i])
        used[i] = 1
        insert_op()
        lst.pop()
        used[i] = 0

n = int(input())
arr = list(map(int,input().split()))
op = list(map(int,input().split()))
op2 = []
lst = []
used = [0 for _ in range(n-1)]
used2 = {}
res = []


for i in range(op[0]):
    op2.append('+')
for i in range(op[1]):
    op2.append('-')
for i in range(op[2]):
    op2.append('*')
for i in range(op[3]):
    op2.append('/')

insert_op()

print(max(res))
print(min(res))