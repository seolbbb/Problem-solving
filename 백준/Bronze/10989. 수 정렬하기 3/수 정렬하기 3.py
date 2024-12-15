#첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 
#둘째 줄부터 N개의 줄에는 수가 주어진다. 
#이 수는 10,000보다 작거나 같은 자연수이다.
#수의 개수와 범위가 정해져있기 때문에 계수 정리 사용.

import sys

n = int(input())

cnt = [0] * 10001

for _ in range(n): # 반복문에서 변수에 _ 사용하면 변수 없이 반복문 사용 가능.(메모리 절약)
    num = int(sys.stdin.readline())
    cnt[num] += 1

for i in range(1, 10001):
    if cnt[i] != 0:
        for _ in range(cnt[i]):
            print(i)