n,m=map(int,input().split(' '))
array=list(map(int,input().split()))

s=0
e=max(array)

result=0

while(s<=e):
    total=0
    mid=(s+e)//2
    for x in array:
        if x>mid:
            total+=x-mid
    if total<m:
        e=mid-1
    else:
        s=mid+1
        result=mid
        
        
        
        
print(result)
