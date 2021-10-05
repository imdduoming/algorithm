import sys
input=sys.stdin.readline
N,M=map(int,input().split())

INF=int(10**9)
graph=[[INF for i in range(N+1)]for j in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    if a==b:
        graph[a][b]=0
    else:
        graph[a][b]=1
        graph[b][a]=1
for i in range(1,N+1):
    graph[i][i]=0
for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
            #print('k:',k,'a:',a,'b:',b,'graph[a][b]',graph[a][b])
min=5000
min_index=0
for a in range(1,N+1):
    sum=0
    for b in range(1,N+1):

        #print('graph[a][b]:',graph[a][b])
        sum=graph[a][b]+sum

    if min>sum:
        min=sum
        min_index=a

   #     print('min:',min,'min_index:',min_index)

print(min_index)

