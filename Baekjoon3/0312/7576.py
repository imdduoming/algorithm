import sys
import collections
input=sys.stdin.readline
M,N=map(int,input().split())

def bfs():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    while queue:
        y,x=queue.popleft()
        #queue2=collections.deque()
        for i in range(4):
            nx=dx[i]+x
            ny=dy[i]+y
            if nx>=0 and nx<M and ny>=0 and ny<N:
                if tomato[ny][nx]==0:
                    tomato[ny][nx]=tomato[y][x]+1
                    queue.append((ny,nx))
    

tomato=[]
for i in range(N):
    garo=list(map(int,input().split()))
    tomato.append(garo)


queue=collections.deque()
for i in range(N):
    for j in range(M):
        if tomato[i][j]==1:
            queue.append((i,j))

bfs()
can=1
result=-2
for i in tomato:
    for j in i:

        if j==0:
            can=0
            break
        result=max(result,j)
if can==0:
    print(-1)

else:
    print(result-1)
