n=int(input())
a=[]
for i in range(n):
    data=input().split()
    a.append((data[0],int(data[1])))

a=sorted(a,key=lambda x: x[1])

for i in range (len(a)):
    print(a[i][0], end= ' ')
