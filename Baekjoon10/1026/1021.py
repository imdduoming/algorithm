# 데크
import sys
from collections import deque

input = sys.stdin.readline  # 빠른 입력
N, M = map(int, input().split())
loc = list(map(int, input().split()))

deque = deque([i for i in range(1, N+1)])

find = 0
count = 0


while (True):

    if deque[0] == loc[find]:
        deque.popleft()
        find += 1
        if find == M:
            break
    else:

        if deque.index(loc[find]) < abs(deque.index(loc[find]) - len(deque)):
            deque.append(deque.popleft())
        else:
            # 3번의 경우
            deque.appendleft(deque.pop())
        count += 1

print(count)