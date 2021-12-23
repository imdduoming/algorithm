#백준 2805 나무자르기

import sys

N, M = map(int, sys.stdin.readline().split())
H = list(map(int, sys.stdin.readline().split()))



start = 0
end = max(H)
max_H = 0

while start <= end:
    get = 0
    mid = (start + end) // 2

    get=0
    for i in range(N):
        if H[i]-mid> 0:
             get += H[i] - mid

    if get >= M:
        max_H = max(max_H, mid)
        start = mid + 1
    else:
        end = mid - 1

print(max_H)