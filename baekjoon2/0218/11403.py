
#플로이드워셜알고리즘
'''
모든 노드에서 다른 모든 노드까지의 최단경로를 확인
2차원 최단거리테이블을 초기화
'''
import sys
input=sys.stdin.readline

N=int(input())
INF=int(10**9)
graph=[[0] for i in range(N+1)]
for i in range(1,N+1):
    arr=list(map(int,input().split()))
    graph[i]=graph[i]+arr
#print(graph)
#route=[[INF for j in range(N+1)] for i in range(N+1)]
#print(route)
for k in range(1,N+1):
    for a in range(1,N+1):
        for b in range(1,N+1):
            if graph[a][k]!=0 and graph[k][b]!=0:
                graph[a][b]=max(graph[a][b],graph[a][k]+graph[k][b])



for i in range(1,N+1):
    for j in range(1,N+1):
        if graph[i][j]==0:
            print(0,end=' ')
        else:
            print(1,end=' ')
    print()


