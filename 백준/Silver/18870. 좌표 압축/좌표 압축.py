import sys

n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().split()))
lst_sort = sorted(lst,reverse=True)
nums = {}

for key in lst_sort:
    nums[key] = 1

k = len(nums)-1

for key in nums.keys():
    nums[key] = k
    k -= 1

for key in lst:
    print(nums[key], end = ' ')