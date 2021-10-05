import sys
import collections
input = sys.stdin.readline #빠른 입력
T=int(input())
def solve():
    queue=collections.deque()
for i in range(T):
    N,M=map(int, input().split())
    queue = []
    queue_s=[0 for row in range(N)]
    count=0
    arr=list(map(int,input().split()))
    #idx=M-1 #몇번 째로 인쇄되는지 궁금한 큐의 인덱스
    for j in arr:
        queue.append(j)
    queue_s[M]=1
    while True:

        if (max(queue)==queue[0]):
            count += 1
            if (queue_s[0] == 1):

                break
            else:
                del queue[0]
                del queue_s[0]


        else:
            queue.append(queue[0])
            del queue[0]
            queue_s.append((queue_s[0]))
            del queue_s[0]


    print(count)
