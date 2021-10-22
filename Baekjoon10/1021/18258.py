# 큐,덱 알고리즘
# 백준18258
#단어공부
import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
queue=deque()
def command(str):

    if str.rsplit(' ')[0]=='push':

        queue.append(int(str.split(' ')[1].rstrip()))

    elif str.rstrip()=='pop':

        if len(queue) == 0:
            print(-1)
        else:

            num=queue.popleft()
            print(num)
    elif str.rstrip() == 'size':

        print(len(queue))

    elif str.rstrip() == 'empty':
        if len(queue)==0:
            print(1)
        else:
            print(0)
    elif str.rstrip() == 'front':
        if len(queue)==0:
            print(-1)
        else:
            num=queue.popleft()
            print(num)
            queue.appendleft(num)

    elif str.rstrip() == 'back':
        if len(queue)==0:
            print(-1)
        else:
            num = queue.pop()
            print(num)
            queue.append(num)



for i in range(N):
    command(input())
