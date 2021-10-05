#최소비용 구하기
import sys
import sys
import heapq
input = sys.stdin.readline #빠른 입력
INF=int(10**9)

N=int(input()) #도시 갯수
M=int(input())
graph=[[] for i in range(N+1)]
distance=[INF] *(N+1)

for i in range(M):
    start,end,cost=map(int,input().split())
    graph[start].append((end,cost))

depart,arrive=map(int,input().split())

result=[]
distance[depart]=0
sum=0

heap = [(0, depart)]
while heap:
    weight, node = heapq.heappop(heap)
    if distance[node]<weight:
        continue

    for i in graph[node]:
        sum=weight+i[1]
        if sum<distance[i[0]]:
            distance[i[0]]=sum
            heapq.heappush(heap,(sum,i[0]))

print(distance[arrive])





