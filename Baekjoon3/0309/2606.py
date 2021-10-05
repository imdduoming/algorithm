import sys
input=sys.stdin.readline
N=int(input()) #컴퓨터의수
M=int(input())
graph=[[] for i in range(N+1)]
visited=[False]*N

def dfs(graph,v,visited):
    global cnt

    visited[v]=True

    for i in graph[v]:
        if visited[i]!=True:
            cnt+=1
            dfs(graph,i,visited)
    return cnt

for i in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
cnt=0

print(dfs(graph,1,visited))
