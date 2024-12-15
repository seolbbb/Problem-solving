import sys

n, m = map(int,sys.stdin.readline().split())

n_lst = list(map(int,sys.stdin.readline().split()))

# 아래 코드의 경우 시간복잡도 O(n*m)으로 100억이 넘음. 시간초과

# for i in range(m):
#     x = list(map(int,sys.stdin.readline().split()))
#     print(sum(n_lst[x[0]-1:x[1]]))

# 누적합 알고리즘을 사용하면 된다.
# 누적합이란, list 안에 들어있는 값의 0~1, 0~2, 0~3, ... , 0~m 까지의 누적합을
# 모두 미리 계산해놓고, 필요할 때 인덱싱 해서 쓰는것이다.
# 처음에 누적합 계산할 때 O(m)이 들고, 그 후 사용할 때는 O(1)이기 때문에
# 시간 복잡도를 크게 줄일 수 있다.

pre = [0 for _ in range(n+1)]

for i in range(1,n+1):
    pre[i] = pre[i-1] + n_lst[i-1]

for i in range(m):
    x, y = map(int,sys.stdin.readline().split())
    print(pre[y] - pre[x-1])