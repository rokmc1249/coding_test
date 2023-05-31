def binary_search(array,target,start,end):
    while start<=end:
        
        mid=(start+end)//2

        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None


n=int(input())

arr=list(map(int,input().split()))
arr.sort()

m=int(input())

arr1=list(map(int,input().split()))
arr1.sort()

for i in arr1:

    r=binary_search(arr,i,0,n-1)

    if r==None:
        print("no",end=' ')
    else:
        print("yes",end=' ')
