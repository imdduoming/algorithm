#최단경로 알고리즘
import sys
import heapq
input = sys.stdin.readline #빠른 입력
INF=int(10**9)
V,E=map(int,input().split())
start=int(input()) #시작점
graph=[[] for i in range(V+1)] #초기값 무한대로 설정
for i in range(E):
    u,v,w=map(int,input().split())

    graph[u].append((v,w))

#거리가 작은 원소가 큐에서 먼저 나올 수 있도록 큐가 구성된다(우선순위 큐)
heap=[(0,start )] #우선순위 큐
dist=[INF]*(V+1)
dist[start]=0
while heap:
    #최단거리가 가장 짧은 노드가 제일 먼저 나옴
    weight,node=heapq.heappop(heap)
    #별도의 방문처리를 위한 테이블이 사용되지 않고 현재 꺼낸 거리의 값이 테이블에 기록되어 있는 값보다 크다면 이미 처리가 된 것으로
    #간주할 수 있음 (원래 무한대로 초기화되어잇기때문)
    if dist[node] > weight:
        continue

    for j in  graph[node]:
        sum=weight+j[1]
        #print(j[0],j[1])
        #현재노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
        if sum <dist[j[0]]:
            dist[j[0]]=sum
            heapq.heappush(heap,(sum,j[0]))

for i in range(1,V+1):
    if dist[i]!=INF:
        print(dist[i])
    else:
        print('INF')






