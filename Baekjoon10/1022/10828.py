#백준 10828 스택
#스택 알고리즘
import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
stack=[]
def command(str):

    if str.rsplit(' ')[0]=='push':

        stack.append(int(str.split(' ')[1].rstrip()))

    elif str.rstrip()=='pop':

        if len(stack) == 0:
            print(-1)
        else:

            num=stack.pop()
            print(num)
    elif str.rstrip() == 'size':

        print(len(stack))

    elif str.rstrip() == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif str.rstrip() == 'top':
        if len(stack)==0:
            print(-1)
        else:
            num=stack[-1]
            print(num)






for i in range(N):
    command(input())
