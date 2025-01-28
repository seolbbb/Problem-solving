import sys
sys.setrecursionlimit(10**7)

def pretopost(start, end):
    if start > end:
        return
    mid = end + 1

    for i in range(start+1, end+1):
        if pre[i] > pre[start]:
            mid = i
            break
    pretopost(start+1,mid-1)
    pretopost(mid, end)
    print(pre[start])

pre = []

while True:
    try:
        node = int(input())
        pre.append(node)
    except:
        break

pretopost(0, len(pre)-1)