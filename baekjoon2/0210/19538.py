import collections
import sys

input = sys.stdin.readline #빠른 입력
N=int(input())
adj=[[]for i in range(N+1)]

for i in range(1,N+1):
    nums=list(map(int,input().split()))
    nums.pop()
    adj[i]=nums
#print(adj)
queue=collections.deque()
M=int(input()) #최초유포자의 수
first=list(map(int,input().split()))
check=[-1 for i in range(N+1)]

for i in first:
    queue.append((i,0))
    check[i]=0

#print(queue)
adjqueue=collections.deque() #인접한 노드의 큐
near=[0 for i in range(N+1)]
while(queue):
    for i in range(0,len(queue)):
        start=queue[i][0]
        time=queue[i][1]
        queue.popleft()
        for j in range(0,len(adj[start])):
            nextnode=adj[start][j]
            if check[nextnode]==-1:
                adjqueue.append((nextnode,time+1))
                














