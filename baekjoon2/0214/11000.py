import sys
import heapq
input = sys.stdin.readline #빠른 입력
N=int(input())
heap=[]
classArr=[]
for i in range(N):
    start,end=map(int,input().split())
    classArr.append((start,end))

classArr=sorted(classArr,key=lambda x:x[0])
heap=[]
for start,end in classArr:
#    print('end:',end,'start:',start)
    if len(heap)!=0:
        if heap[0]<=start:
            heapq.heappop(heap)
        heapq.heappush(heap, end)


    else:
        heapq.heappush(heap,end)


print(len(heap))


