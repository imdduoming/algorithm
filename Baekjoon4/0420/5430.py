import sys
import collections
input=sys.stdin.readline
T=int(input())
def solve(order,arr):
    r_count=0
    d_count=0
    direct=1
    err=0


    for i in order:
        if i=='R':
            r_count+=1
            if direct==1:
                direct=0
            else:
                direct=1

        elif i=='D':
            if len(arr)==0:
                err=1
                break
            if direct==1:
                arr.popleft()
            else:
                arr.pop()
    if r_count%2==1:
        arr.reverse()

    if err==1:
        return 0
    else:
        return arr


for i in range(T):
    order=input().strip()
    len_arr=int(input())
    arr = sys.stdin.readline()[1:-2].split(",")

    if arr[0] != '':
        arr = collections.deque(arr)
    else:
        arr = collections.deque()

    r_count = 0
    d_count = 0
    direct = 1
    err = 0

    for i in order:
        if i == 'R':
            r_count += 1
            if direct == 1:
                direct = 0
            else:
                direct = 1

        elif i == 'D':
            if len(arr) == 0:
                err = 1
                break
            if direct == 1:
                arr.popleft()
            else:
                arr.pop()

    if r_count % 2 == 1:
        arr.reverse()
    if err!=1:
        print('[', end='')
        for i in range(len(arr)):
            print(arr[i], end='')
            if i != len(arr) - 1:
                print(",", end='')
        print("]")
    else:
        print('error')

