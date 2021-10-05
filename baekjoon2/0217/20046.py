import sys
import heapq
input = sys.stdin.readline #빠른 입력
m,n=map(int,input().split())
INF=int(10**9)
road=[0 * n+1]
for i in range(m):
    col=[0]
    arr=list(map(int,input().split()))
    col=col+arr
    road.append(col)
dx=[-1,0,1,0]
dy=[0,-1,0,1]
check=[[INF for i in range(n+1)] for j in range(m+1)]
heap=[(road[1][1],(1,1))]


while heap:
    now=heapq.heappop(heap)
    x=now[1][1]
    y=now[1][0]
    num=now[0]
    #print('x:',x,'y:',y,'num:',num)
    if check[y][x]<=num:
        continue
    check[y][x]=num
    if x==n and y==m:
        break
    for i in range(0,4):
        next_x=x+dx[i]
        next_y=y+dy[i]
        #print('next_x: ',next_x,'next_y: ',next_y)
        if next_x>=1 and next_y>=1 and next_y<=m and next_x<=n:
            next_num=num+road[next_y][next_x]

            if next_num<check[next_y][next_x] and road[next_y][next_x]!=-1 :
                heapq.heappush(heap,(next_num,(next_y,next_x)))
        #print(heap)

if road[1][1]==-1 or road[m][n]==-1:
    print(-1)
elif check[m][n]==INF:
    print(-1)
else:
    print(check[m][n])






