import sys
import collections
input=sys.stdin.readline
N=int(input())
apart=[]
def bfs(y,x,apart,danji,cnt):

    queue=collections.deque()
    queue.append((y,x))
    #print('x:',x,'y:',y,'cnt:',cnt)

    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    while queue:
        y,x=queue.popleft()
        for i in range(4):

            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if apart[ny][nx]==1: #집 존재하는경우

                    apart[ny][nx]=True #방문표시
                    danji[cnt]+=1
                    print('apart[',ny,'][',nx,']','=',cnt)
                    queue.append((ny,nx))


for i in range(N):
    col=list(map(int,input().rstrip()))
    apart.append(col)


cnt=1
danji=[0 for i in range(26)]
for i in range(N):
    for j in range(N):
        if apart[i][j]!=True: #방문하지 않은경우에만
            bfs(j,i,apart,danji,cnt)
            cnt+=1




for k in range(1,26):
    if danji[k]==0:
        break
    else:
        print(danji[k])


