import math
A, B, V = map(int,input().split())

l = A - B
n = math.ceil((V - B) / l)

print(n)