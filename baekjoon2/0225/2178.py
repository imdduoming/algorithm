import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())
#graph=[[-1 for i in range(M+1)] for j in range(N+1)]
def bfs(x,y):
    queue=deque()
    queue.append((x,y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue

            if graph[nx][ny]==0:
                continue

            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
               # print('graph[nx][ny]',graph[nx][ny])
                queue.append((nx,ny))

                #print(queue)

    return graph[N-1][M-1]


graph=[]
for i in range(0,N):
    graph.append(list(map(int,input().rstrip())))

#print(graph)

print(bfs(0,0))