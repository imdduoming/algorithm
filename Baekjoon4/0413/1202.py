#그리디 알고리즘
#우선순위 큐사용

import sys
import heapq
input=sys.stdin.readline
N,K=map(int,input().split())
jewerly=[]
for i in range(N):
    weight,val=map(int,input().split())
    heapq.heappush(jewerly,(weight,val))
#print(jewerly)

bag=[]
for i in range(K):
    capacity=int(input())
    heapq.heappush(bag,capacity)

capable=[] #현재 bag의 capacity 보다 작은 모든 보석들
total=0

for i in range(K):
    #현재 bag의 수용량
    capacity=heapq.heappop(bag)

    while jewerly and capacity>=jewerly[0][0]:
        weight,value=heapq.heappop(jewerly)
        heapq.heappush(capable,-value) #무게로 최대힙구성

    if capable:
        total-=heapq.heappop(capable)
    elif not jewerly: #더이상 bag에 넣을 수 있는 보석이 없을 때
        break

print(total)

