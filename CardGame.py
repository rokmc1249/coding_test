n,m=map(int,input().split())
r=0
for i in range(n):
    data=list(map(int,input().split()))
    data.sort()
    min_v=data[0]
    r=max(min_v,r)
print(r)
    
