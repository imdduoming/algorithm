import sys
import heapq

input=sys.stdin.readline
N=int(input())

heap=[]



heapq.heapify(heap)

for i in range(N):
    num=int(input())
    if num != 0:
        heapq.heappush(heap, (abs(num),num)) #절댓값이 작은거부터 들어갈 수 있도록 절대값이 같은 경우 더 작은 숫자가 먼저
    else:
        if len(heap) == 0:
            print(0)
        else:
            abs_num,real_num=heapq.heappop(heap)
            print(real_num)

