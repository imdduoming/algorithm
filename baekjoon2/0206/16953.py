import sys
import collections
input = sys.stdin.readline #빠른 입력
A,B=map(int,input().split())


def bfs(start,end):
    queue = collections.deque()

    discovered=[start]
    found_flag=0
    queue.append((A,1))

    while queue:
        num,count=queue.popleft()
        if num==B:
            found_flag=1
            break
        if num*2<=B:
            queue.append((num*2,count+1))
        if num*10+1<=B:
            queue.append(((num*10)+1,count+1))
        print(queue)


    if found_flag:
        return count
    else:
        return -1
print(bfs(A,B))