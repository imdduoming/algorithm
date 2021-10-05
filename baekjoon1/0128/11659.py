import sys
input = sys.stdin.readline #빠른 입력
N, M = map(int, input().split())
nums=list(map(int,input().split()))
sum=0
pre=[0]*(N+1)
for i in range(N):
    sum=sum+nums[i]
    pre[i+1]=sum

ans=0

for i in range(M):
    a,b=map(int,input().split())
    ans=pre[db]-pre[a-1]
    print(ans)