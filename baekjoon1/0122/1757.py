import sys

N,M=map(int,sys.stdin.readline().split())

nums=[0]*10001
for i in range(1,N+1):
    nums[i]=int(input())

dp = [[[0]*2 for _ in range(M+5)] for _ in range(N+5)]

for level in range(1,N+1):
    for count in range(0,M+1):
        if(count==0):
            #달리다가 쉬거나 쉬다가 쉬거나
            #지침지수가 0이면서 달릴 수는 없는거임
            dp[level][0][0] = max(dp[level-1][count+1][1], dp[level-1][count+1][0],dp[level-1][count][0])
        elif(count==1):
            # 달리고 있던 상태에서 다시 달리거나 쉬다가 달리는거 가능
            dp[level][count][1] = max(dp[level - 1][count - 1][1],dp[level-1][count-1][0])+nums[level]
            # 달리다가 쉬거나 쉬다가 쉴 수 있음
            dp[level][count][0] = max(dp[level - 1][count + 1][1], dp[level - 1][count + 1][0])


        else:
            #달리고 있던 상태에서 다시 달림( 쉬다가 달리는 경우는 지침지수가 1일 경우 밖에 없음  )
            dp[level][count][1] = dp[level-1][count -1][1] + nums[level]
            #달리다가 쉬거나 쉬다가 쉴 수 있음
            dp[level][count][0]= max(dp[level-1][count+1][1],dp[level-1][count+1][0])

print(dp[N][0][0])
