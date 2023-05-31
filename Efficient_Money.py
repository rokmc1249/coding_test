n,m=map(int,input().split())

a=[]
for i in range(n):
    a.append(int(input()))

d=[10001]*(m+1)

d[0]=0

for i in range(n): #i는 화폐의 단위
    for j in range(a[i],m+1): #j는 금액
        if d[j-a[i]]!=10001:
            d[j]=min(d[j],d[j-a[i]]+1)

if d[m]==10001:
    print(-1)
else:
    print(d[m])
