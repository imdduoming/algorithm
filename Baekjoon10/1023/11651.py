N=int(input())
points=[]
for i in range(N):
    x,y=map(int,input().split(' '))
    points.append((x,y))
points.sort(key=lambda x:(x[1],x[0]))

for i,j in points:
    print(i,j)