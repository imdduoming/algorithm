import sys
input = sys.stdin.readline #빠른 입력
N, M = map(int, input().split())
nums=list(map(int,input().split()))
count=0

left=0
right=1
sum=nums[left]

while left<N:

    if sum==M:
        count+=1
        sum-=nums[left]
        left+=1

    if right==N and sum<M:
        break
    elif sum<M:
        sum += nums[right]
        right+=1


    else:
        sum-=nums[left]
        left+=1

print(count)