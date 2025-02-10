n = int(input())

line = [0 for _ in range(n)]

lst = list(map(int, input().split()))

# 첫자리부터 마지막까지 확인. 빈자리(0) 갯수가 lst 값과 같아지면 그 자리에 넣음.
# 
for i in range(len(lst)):
    cnt = -1

    for j in range(len(line)):
        if line[j] == 0:
            cnt += 1
            if cnt == lst[i]:
                line[j] = i+1

print(' '.join(map(str, line)))