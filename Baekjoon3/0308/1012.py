import sys
import collections
input=sys.stdin.readline
T=int(input())
def bfs(farm,farmcount=0):

    queue=collections.deque()
    farmcnt=0
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]

    for i in range(0,N):
        for j in range(0,M):

            if farm[i][j]==1:

                queue.append((i,j))
                farm[i][j]=-1 #방문체크
                while True:
                    y,x=queue.pop()
                    for k in range(0,4):
                        nx=x+dx[k]
                        ny=y+dy[k]


                        if 0<=ny<=N-1 and 0<=nx<=M-1 and farm[ny][nx]==1:
                            #print('nx:', nx, 'ny:', ny)
                            queue.append((ny,nx))
                            farm[ny][nx]=-1

                    if not queue:
                        farmcnt+=1
                        break
    return farmcnt


for j in range(T):
    M,N,K=map(int,input().split())
    farm=[[0 for i in range(M)] for j in range(N)]
    #print(farm)
    for i in range(K):
        x,y=map(int,input().split())
        farm[y][x]=1

    farmcount=0

    print(bfs(farm,farmcount))

