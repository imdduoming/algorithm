import sys
import collections
input = sys.stdin.readline #빠른 입력
A,B=map(int,input().split())


def bfs(start,end):
    queue = collections.deque()
    visited=set()
    found_flag=0
    queue.append((A,0))

    while queue:
        num,count=queue.popleft()
        #print('num: ',num,'count: ',count)
        if num==end:
            found_flag=1
            break


        if num-1>=0 and num-1 not in visited:
            queue.append((num-1,count+1))
            visited.add(num-1)

        if num+1 < 100001 and num+1 not in visited:
            queue.append((num+1,count+1))
            visited.add(num +1)

        if num*2<100001 and num*2 not in visited:
            queue.append((num* 2, count + 1))
            visited.add(num*2)
        #print(queue)
    if found_flag:
        return count
    else:
        return -1
print(bfs(A,B))