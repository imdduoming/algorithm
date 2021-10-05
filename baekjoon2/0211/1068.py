import sys
import collections
input = sys.stdin.readline #빠른 입력
N=int(input())
parent=list(map(int,input().split()))
delete=int(input())

delnode={}
delnode[delete]=0
tree ={}
count=0
for i in range(N):
    if i==delete or parent[i] in delnode:
        if parent[i] in delnode:
            if i not in delnode:
                delnode[i]=0
        continue
    else:
        if parent[i] in tree:
            tree[parent[i]].append(i)
        else:
            tree[parent[i]]=[i]
print('tree:',tree)
#print('delnode:',delnode)


if -1 in tree:
    queue=[-1]
else:
    queue=[]
while queue:
    node=queue.pop()
    if node not in tree:
        count+=1
    else:
        queue+=tree[node]

print(count)
