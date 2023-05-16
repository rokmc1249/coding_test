n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))

#a.sort()
#a.reverse()

a=sorted(a,reverse=True)
for i in range(len(a)):
    print(a[i], end= ' ')

