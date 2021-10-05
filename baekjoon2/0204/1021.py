# 데크
import sys
import collections
input = sys.stdin.readline #빠른 입력
N,M=map(int,input().split())
loc=list(map(int,input().split()))
loc_dict={}
for i in loc:
    loc_dict[i]=0
find=0
deque=collections.deque()

for i in range(1,N+1):
    deque.append(i)
    i+=1

count=0
j=0

while(True) :

    if deque[0] ==loc[find]:
        deque.popleft()
        find+=1
        if find == M:

            break


    else:

        if deque.index(loc[find]) < abs(deque.index(loc[find])- len(deque)):
            deque.append(deque.popleft())
        else:
         #3번의 경우
            deque.appendleft(deque.pop())
        count+=1


print(count)