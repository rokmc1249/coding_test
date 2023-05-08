n=int(input())
data=input().split()
x,y=1,1
moves=["L","R","U","D"]

for i in data:
    for j in range(len(moves)):    
    
        if(i==moves[0]):
            nx=x+0
            ny=y-1
        elif(i==moves[1]):
            nx=x+0
            ny=y+1
        elif(i==moves[2]):
            ny=y+0
            nx=x-1
        elif(i==moves[3]):
            ny=y+0
            nx=x+1
    if(nx<1 or ny < 1 or nx>n or ny>n):
        continue
    x,y=nx,ny
print(x,y)
