n,m,k=map(int,input().split())
arr=list(map(int,input().split()))

arr.sort()
first=arr[n-1]
sec=arr[n-2]
r=0
while True:
    
    for i in range(k):
        if m==0:
            break
        r=r+first
        m-=1
    if m==0:
        break
    r+=sec
    m-=1
print(r)
