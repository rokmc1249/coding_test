position=input()
r=int(position[1])
c=int(ord(position[0]))-int(ord('a'))+1
count=0

step=[(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]

for i in step:
    dx=c+i[0]
    dy=r+i[1]
    
    if(dx<1 or dy<1 or dx>8 or dx>8):
        continue
    count+=1
print(count)
    

