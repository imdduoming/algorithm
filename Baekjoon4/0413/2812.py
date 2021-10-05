#크게만들기
#그리디알고리즘
import sys
input=sys.stdin.readline
N,K=map(int,input().split())
num=list(input().rstrip())



stack=[]
k=K
for i in range(N):
    while k>0 and stack and stack[-1]<num[i]:
        stack.pop()
        k-=1
    stack.append(num[i])
print(''.join(stack[:N-K]))