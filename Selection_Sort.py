a=[7,5,9,0,3,1,6,2,4,8]


for i in range(len(a)):
    mina=i
    for j in range(i+1,len(a)):
        if a[mina]>a[j]:
            mina=j
    a[mina],a[i]=a[i],a[mina]
print(a)
