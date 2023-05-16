n,k=map(int,input().split())
arr=list(map(int,input().split()))
brr=list(map(int,input().split()))

arr.sort()
brr.sort(reverse=True)

for i in range(k):
    if arr[i]<brr[i]:
        arr[i],brr[i]=brr[i],arr[i]
    else:
        break

print(sum(arr))

