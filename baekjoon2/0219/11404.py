#플로이드워셜알고리즘
'''
모든 노드에서 다른 모든 노드까지의 최단경로를 확인
2차원 최단거리테이블을 초기화
'''
import sys
input=sys.stdin.readline

N=int(input())
M=int(input()) #버스의 개수
INF=int(10**9)
graph=[[INF for i in range(N+1)]for j in range(N+1)]
for i in range(M):
    start,end,cost=map(int,input().split())
    if graph[start][end]!=INF:
        graph[start][end]=min(cost,graph[start][end])
    else:
        graph[start][end]=cost


for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            if a==b:
                graph[a][b]=0
            else:
                graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])



for i in range(1,N+1):
    for j in range(1,N+1):
        if graph[i][j]==INF:
            print(0,end=' ')
        else:
            print(graph[i][j],end=' ')
    print()


