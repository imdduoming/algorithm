#현재상황에서 가장 작은 두개를 더해야하는 것이 핵심 알고리즘이다
import sys
import heapq
input=sys.stdin.readline
N=int(input())
card=[]
for i in range(N):
    heapq.heappush(card,int(input()))

card.sort()
if len(card)<=1:
    print(0)
else:
    sum=0
    while len(card)>1:

        first=heapq.heappop(card)
        second=heapq.heappop(card)
        sum=sum+first+second
        #print('sum:',sum,'first:',first)
        heapq.heappush(card,first+second)

    print(sum)

