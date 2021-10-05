import sys
import collections
input = sys.stdin.readline #빠른 입력

N=int(input())
tree=[[] for i in range(N)]

for i in range(0,N-1):
    parent,child,val=map(int,input().split())
    tree[parent-1].append([child-1,val])
    tree[child-1].append([parent-1,val])

def bfs(start,m):
    queue=collections.deque()
    queue.append(start)

    visited=[-1 for i in range(N)]
    visited[start]=0

    while queue:
        start=queue.popleft()
        for child,val in tree[start]:
            if visited[child]==-1:
                visited[child]=visited[start]+val
                queue.append(child)
    if m==1:
        return visited.index(max(visited))
    else:
        return max(visited)


print(bfs(bfs(0,1),2))
