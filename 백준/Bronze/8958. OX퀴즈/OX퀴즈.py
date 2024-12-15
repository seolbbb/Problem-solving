n = int(input())

for i in range(n):
    A = list(input())
    Sum = 0
    cnt = 0
    for j in range(len(A)):
        if A[j] == 'O':
            Sum += cnt + 1
            cnt += 1
        elif A[j] == 'X':
            cnt = 0
    print(Sum)