a=[7,5,9,0,3,1,6,2,4,8]

def quick(a):
    if len(a)<=1:
        return a
    pivot=a[0]
    tail=a[1:]

    left=[x for x in tail if x<=pivot]
    right=[x for x in tail if x>pivot]

    return quick(left) + [pivot] + quick(right)
print(quick(a))
