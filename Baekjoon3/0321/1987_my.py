import sys

input=sys.stdin.readline

def dfs(x,y,cnt):
    global ans
    ans=max(ans,cnt)

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if 0<=nx<R and 0<=ny<C and check[board[nx][ny]]!=1:
               #범위안에있고 방문하지 않았을 때
            check[board[nx][ny]]=1
            dfs(nx,ny,cnt+1)
            check[board[nx][ny]]=0


R,C=map(int,input().split())

dx=(0,0,1,-1)
dy=(1,-1,0,0)


board=[list(map(lambda x:ord(x)-65,input().rstrip())) for _ in range(R)]

check=[0]*26
ans=0
check[board[0][0]]=1
dfs(0,0,1)
print(ans)