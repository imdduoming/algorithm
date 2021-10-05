import sys
import collections
input = sys.stdin.readline #빠른 입력
N=int(input())
tree=[[] for j in range(100001)]
#tree=collections.deque()

for i in range(N-1):
     a,b=map(int ,input().split())
     tree[a].append(b)
     tree[b].append(a)


visited=[-1 for i in range(100001)]
parent={}
queue=[1]
while queue:
    node=queue.pop()
    for i in tree[node]:
        if visited[i]==-1:
           visited[i]=1 # 방문
           parent[i]=node
           queue.append(i)
for i in range(2,N+1):
    print(parent[i])

