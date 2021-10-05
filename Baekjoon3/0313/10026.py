import sys
import collections
input=sys.stdin.readline
N=int(input())
color=[]


def bfs(y,x,color,val):

    global cnt

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
                if color[ny][nx]==val: #같은색일경우
                    color[ny][nx]=0 #방문표시
                    queue.append((ny,nx))







for i in range(N):
    col=list(input().rstrip())
    color.append(col)

color_rg=[[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        if color[i][j]=='R' or color[i][j]=='G':
            color_rg[i][j]=1
        else:
            color_rg[i][j]=2
cnt=0
cnt_rg=0
for i in range(N):
    for j in range(N):
        if color[i][j]!=0: #일반 방문 확인
            cnt+=1
            bfs(i,j,color,color[i][j])
        if color_rg[i][j]!=0: #일반 방문 확인
            cnt_rg+=1
            bfs(i,j,color_rg,color_rg[i][j])
print(cnt,cnt_rg)