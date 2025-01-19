import sys
input = sys.stdin.readline

def calc(a, b, op_type):
    # op_type: 0->+, 1->-, 2->*, 3->/
    if op_type == 0:
        return a + b
    elif op_type == 1:
        return a - b
    elif op_type == 2:
        return a * b
    else:  
        if a < 0:
            return -(-a // b)
        else:
            return a // b

def dfs(idx, value):

    if idx == n-1:
        results.append(value)
        return

    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            new_value = calc(value, arr[idx+1], i)
            dfs(idx+1, new_value)
            operators[i] += 1

n = int(input())
arr = list(map(int, input().split()))
operators = list(map(int, input().split()))
results = []

dfs(0, arr[0])

print(max(results))
print(min(results))