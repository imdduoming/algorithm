import sys
input=sys.stdin.readline
N=int(input())
nums=[]
answer=0
for i in range(N):
    num=float(input())
    nums.append(num)
    #한번도 연속으로 곱하지 않는 경우가 답이 될 수도 있으므로 초기 최댓값 세팅은 입력받는 가운데 가장 큰 수로 해둔다
    answer=max(answer,num)


for i in range(1,N):
    nums[i]=max(nums[i-1]*nums[i],nums[i])
    answer=max(answer,nums[i])

print(format(answer,'.3f'))

