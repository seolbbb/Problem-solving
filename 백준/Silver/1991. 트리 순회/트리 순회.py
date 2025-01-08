def preorder(node,tree):
    if node != '.':
        print(node, end="")
        preorder(tree[node][0],tree)
        preorder(tree[node][1],tree)

def inorder(node,tree):
    if node != '.':
        inorder(tree[node][0],tree)
        print(node, end="")
        inorder(tree[node][1],tree)

def postorder(node,tree):
    if node != '.':
        postorder(tree[node][0],tree)
        postorder(tree[node][1],tree)
        print(node, end="")

n = int(input())
tree = {}

for _ in range(n):
    root,left,right = input().split()
    tree[root] = [left,right]

preorder('A',tree)
print()
inorder('A',tree)
print()
postorder('A',tree)