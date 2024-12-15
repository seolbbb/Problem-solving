A = int(input())
B = int(input())
C = int(input())
result = A * B * C
result_list = list(map(int, str(result)))

for i in range(0,10):
    print(result_list.count(i))