import sys
N=int(sys.stdin.readline())
dp=[[0 for col in range(1001)] for row in range(1001)]
dp[2][0]=1
dp[2][1]=1
mod=1000000007
for i in range(3,N+1):
    dp[i][0]=(dp[i-1][1]+dp[i-1][2])%mod
    dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % mod
    dp[i][2] = (dp[i - 1][1] + dp[i - 1][0]) % mod


print(dp[N][0])
