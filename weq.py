
array=[9,7,8,10,6]

min=0
max=0
for j in range(1,len(array)):
        if array[min]>array[j]:
            min=j
        elif array[max]<array[j]:
            max=j
print("min",array[min])
print("max",array[max])

