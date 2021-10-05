import sys
N,M=map(int,sys.stdin.readline().split())
dp=[[1 for col in range(1001)] for row in range(1001)]
mod=1000000007
for i in range(2,1001):
    for j in range(2,1001):
        dp[i][j]=(dp[i-1][j]+dp[i][j-1]+dp[i-1][j-1])%mod
    if i==N:
        br

print(dp[N][M])
