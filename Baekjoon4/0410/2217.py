#그리디알고리즘
#로프
import sys
input=sys.stdin.readline
N=int(input())
rope=[]
for i in range(N):
    rope.append(int(input()))

rope.sort()
max_ans=0
for i in range(0,len(rope)):
    max_ans=max((len(rope)-i)*rope[i],max_ans)

print(max_ans)