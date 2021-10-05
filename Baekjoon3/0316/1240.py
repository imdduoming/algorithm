import sys
import collections
input=sys.stdin.readline
N,M=map(int,input().split())


graph=[[] for i in range(N+1)]

for i in range(N-1):
    A,B,dist=map(int,input().split())
    graph[A].append((B,dist))
    graph[B].append((A,dist))




def dfs(start,end,visited,distance,dist):

    visited[start]=True


    for i,j in graph[start]:
        #print('i:',i,'j:',j)
        if i==end:
            distance[start][end]=dist+j
            #print('distance:',distance)
            print(distance[start][end])
            return


        if visited[i]==False:
            
            distance[start][i]=dist+j
            #print('i:',i,'j:',j,'거리:',distance)
            dfs(i,end,visited,distance,dist+j)


distance= [[0 for i in range(N+1)] for j in range(N+1)]

for i in range(M):
    node_a,node_b=map(int,input().split())
    visited = [False] * (N + 1)
  
    dist=0
    dfs(node_a,node_b,visited,distance,dist)
