import sys

n, m = map(int,sys.stdin.readline().split())

n_lst = []
result = []

# sys.stdin.readline()은 개행문자 \n도 같이 입력받는다.

for i in range(n):
    n_lst.append(sys.stdin.readline().rstrip())

n_lst = set(n_lst)

for i in range(m):
    a = sys.stdin.readline().rstrip()
    if a in n_lst:
        result.append(a)

result.sort()

print(len(result))
for x in result:
    print(x)