#그리디알고리즘
#저울
import sys
input=sys.stdin.readline
N=int(input())
choo=list(map(int,input().split()))

choo.sort()
total=0
for i in choo:
    if total+1 <i:
        break
    total=total+i

print(total+1)