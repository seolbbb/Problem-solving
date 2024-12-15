import sys

n = int(input())

x_min = 0
x_max = 0
y_min = 0
y_max = 0

for i in range(n):
    x, y = map(int,sys.stdin.readline().split())

    if i == 0:
        x_max = x
        x_min = x
        y_max = y
        y_min = y

    if x >= x_max:
        x_max = x
    if x <= x_min:
        x_min = x
    
    if y >= y_max:
        y_max = y
    if y <= y_min:
        y_min = y


x = x_max - x_min
y = y_max - y_min

print(x*y)