a,b=map(int,input().split())

x=a//b

while a-b*x<0:
    if b<0:x+=1
    else:x-=1
    
print(x)
print(a-b*x)