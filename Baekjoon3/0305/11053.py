import sys
input=sys.stdin.readline
N=int(input())
nums=list(map(int,input().split()))
#print(nums)
dp=[1]*N
for i in range(0,N):
    for j in range(0,i):
        if nums[i]>nums[j]:
            dp[i]=max(dp[i],dp[j]+1)


max_val=0
for i in dp:
    max_val=max(i,max_val)

print(max_val)