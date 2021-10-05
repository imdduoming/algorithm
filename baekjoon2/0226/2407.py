#조합
#다이나믹 프로그래밍
N,M=map(int,input().split())
dp=[[0 for i in range(N+1)] for j in range(N+1)]

for i in range(N+1):
    for j in range(i+1):
        if j==0 and j==i:
            dp[i][j]=1
        else:
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j]

print(dp[N][M])